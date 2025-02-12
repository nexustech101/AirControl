"""AirControl - Hand gesture-based mouse control."""
from typing import Optional

import cv2

from .config import AirControlConfig
from .core.camera import Camera
from .core.hand_tracker import HandTracker
from .core.mouse import MouseController
from .gestures.click import ClickGesture
from .gestures.drag import DragGesture
from .utils.coordinates import CoordinateTransformer

class AirControl:
    """Main class for hand gesture-based mouse control."""
    
    def __init__(self, config: Optional[AirControlConfig] = None):
        """Initialize AirControl.
        
        Args:
            config: Configuration for AirControl components
        """
        self.config = config or AirControlConfig()
        
        # Initialize components
        self.camera = Camera(self.config.camera)
        self.hand_tracker = HandTracker(self.config.hand_tracking)
        self.mouse = MouseController(self.config.mouse)
        
        # Initialize gestures
        self.click_gesture = ClickGesture(self.config.mouse.click_threshold)
        self.drag_gesture = DragGesture(self.config.mouse.fist_detection_threshold)
        
        # Initialize coordinate transformer
        screen_width, screen_height = self.mouse.get_screen_dimensions()
        self.coordinate_transformer = CoordinateTransformer(
            screen_width,
            screen_height,
            self.config.mouse.speed_multiplier
        )
        
    def process_frame(self) -> bool:
        """Process a single frame from the camera.
        
        Returns:
            bool: True if processing should continue, False if should stop
        """
        # Read frame from camera
        success, frame = self.camera.read_frame()
        if not success:
            return False
            
        # Process frame for hand landmarks
        hand_landmarks, annotated_frame = self.hand_tracker.process_frame(frame)
        
        if hand_landmarks:
            # Get index finger tip coordinates
            index_tip = hand_landmarks.landmark[self.hand_tracker.mp_hands.HandLandmark.INDEX_FINGER_TIP]
            screen_x, screen_y = self.coordinate_transformer.landmark_to_screen(index_tip)
            
            # Detect gestures
            left_click, right_click = self.click_gesture.detect(hand_landmarks)
            is_drag = self.drag_gesture.detect(hand_landmarks)
            
            # Handle mouse actions
            if is_drag:
                self.mouse.start_drag(screen_x, screen_y)
            else:
                self.mouse.end_drag()
                self.mouse.move(screen_x, screen_y)
                
                if left_click:
                    self.mouse.click()
                elif right_click:
                    self.mouse.click(right=True)
        
        # Display frame
        cv2.imshow('AirControl', annotated_frame)
        
        # Check for exit key
        return cv2.waitKey(1) & 0xFF != ord('q')
        
    def run(self) -> None:
        """Run the main processing loop."""
        try:
            while self.process_frame():
                pass
        finally:
            self.cleanup()
            
    def cleanup(self) -> None:
        """Clean up resources."""
        self.camera.release()
        cv2.destroyAllWindows()
