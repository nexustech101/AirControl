"""Base classes for gesture detection."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

import mediapipe as mp
import numpy as np

class BaseGesture(ABC):
    """Base class for all gestures."""
    
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        
    @abstractmethod
    def detect(self, hand_landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> bool:
        """Detect if the gesture is present in the given hand landmarks.
        
        Args:
            hand_landmarks: MediaPipe hand landmarks
            
        Returns:
            bool: True if gesture is detected, False otherwise
        """
        pass
    
    def calculate_distance(self, point1: Any, point2: Any) -> float:
        """Calculate Euclidean distance between two points.
        
        Args:
            point1: First landmark point
            point2: Second landmark point
            
        Returns:
            float: Euclidean distance between points
        """
        return np.sqrt(
            (point1.x - point2.x) ** 2 +
            (point1.y - point2.y) ** 2
        )

class GestureHandler:
    """Base class for handling gesture actions."""
    
    @abstractmethod
    def on_gesture_detected(self, gesture_data: Dict[str, Any]) -> None:
        """Handle detected gesture.
        
        Args:
            gesture_data: Dictionary containing gesture information
        """
        pass
