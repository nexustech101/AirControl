"""Click gesture implementations."""
from typing import Tuple

import mediapipe as mp

from .base import BaseGesture

class ClickGesture(BaseGesture):
    """Detects click gestures based on finger pinching."""
    
    def __init__(self, threshold: float = 0.025):
        super().__init__()
        self.threshold = threshold
    
    def detect(self, hand_landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> Tuple[bool, bool]:
        """Detect both left and right click gestures.
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            Tuple[bool, bool]: (left_click, right_click) detection results
        """
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

        index_distance = self.calculate_distance(index_tip, thumb_tip)
        pinky_distance = self.calculate_distance(pinky_tip, thumb_tip)

        return (index_distance < self.threshold,
                pinky_distance < self.threshold)
