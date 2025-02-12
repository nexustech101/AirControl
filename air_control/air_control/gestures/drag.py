"""Drag gesture implementations."""
import mediapipe as mp

from .base import BaseGesture

class DragGesture(BaseGesture):
    """Detects drag gestures based on fist formation."""
    
    def __init__(self, threshold: float = 0.6):
        super().__init__()
        self.threshold = threshold
        
    def detect(self, hand_landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> bool:
        """Detect if hand is in a fist position (drag gesture).
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if fist is detected, False otherwise
        """
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP,
        ]

        finger_bases = [
            self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
            self.mp_hands.HandLandmark.RING_FINGER_MCP,
            self.mp_hands.HandLandmark.PINKY_MCP,
        ]

        return all(
            hand_landmarks.landmark[tip].y > hand_landmarks.landmark[base].y
            for tip, base in zip(finger_tips, finger_bases)
        )
