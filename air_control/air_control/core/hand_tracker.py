"""Core hand tracking functionality."""
from typing import Optional, Tuple

import cv2
import mediapipe as mp
import numpy as np

from ..config import HandTrackingConfig
from ..utils.coordinates import CoordinateTransformer

class HandTracker:
    """Handles hand tracking and landmark detection."""
    
    def __init__(self, config: HandTrackingConfig):
        """Initialize the hand tracker.
        
        Args:
            config: Configuration for hand tracking
        """
        self.config = config
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=config.static_image_mode,
            max_num_hands=config.max_num_hands,
            min_detection_confidence=config.min_detection_confidence,
            min_tracking_confidence=config.min_tracking_confidence
        )
        
    def process_frame(self, frame: np.ndarray) -> Tuple[Optional[mp.framework.formats.landmark_pb2.NormalizedLandmarkList], np.ndarray]:
        """Process a video frame and detect hand landmarks.
        
        Args:
            frame: Video frame to process
            
        Returns:
            Tuple containing:
                - Hand landmarks if detected, None otherwise
                - Processed frame with landmarks drawn
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            # Draw landmarks on frame
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )
            return results.multi_hand_landmarks[0], frame
            
        return None, frame
