"""Example of creating custom gestures for AirControl."""
import mediapipe as mp

from air_control import AirControl, AirControlConfig
from air_control.gestures.base import BaseGesture

class PinchGesture(BaseGesture):
    """Custom gesture that detects when all fingers are pinched together."""
    
    def __init__(self, threshold: float = 0.1):
        super().__init__()
        self.threshold = threshold
        
    def detect(self, hand_landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> bool:
        """Detect if all fingers are pinched together.
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if gesture is detected, False otherwise
        """
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP,
            self.mp_hands.HandLandmark.THUMB_TIP
        ]
        
        # Calculate distances between all fingertips
        tip_distances = []
        for i in range(len(finger_tips)):
            for j in range(i+1, len(finger_tips)):
                tip1 = hand_landmarks.landmark[finger_tips[i]]
                tip2 = hand_landmarks.landmark[finger_tips[j]]
                distance = self.calculate_distance(tip1, tip2)
                tip_distances.append(distance)
                
        # Check if all fingertips are close together
        return all(distance < self.threshold for distance in tip_distances)

def main():
    # Create configuration
    config = AirControlConfig()
    
    # Create AirControl instance
    controller = AirControl(config)
    
    # Add custom gesture
    pinch_gesture = PinchGesture()
    
    # Modify the process_frame method to use custom gesture
    original_process_frame = controller.process_frame
    
    def custom_process_frame():
        success, frame = controller.camera.read_frame()
        if not success:
            return False
            
        hand_landmarks, annotated_frame = controller.hand_tracker.process_frame(frame)
        
        if hand_landmarks:
            # Check for custom gesture
            if pinch_gesture.detect(hand_landmarks):
                # Perform custom action when gesture is detected
                print("All fingers pinched!")
                
        return original_process_frame()
    
    # Replace process_frame with custom version
    controller.process_frame = custom_process_frame
    
    # Run the controller
    controller.run()

if __name__ == "__main__":
    main()
