"""Coordinate transformation utilities."""
from typing import Tuple

import mediapipe as mp
import numpy as np

class CoordinateTransformer:
    """Handles coordinate transformations between different spaces."""
    
    def __init__(self, screen_width: int, screen_height: int, speed_multiplier: float = 1.5):
        """Initialize the coordinate transformer.
        
        Args:
            screen_width: Width of the screen in pixels
            screen_height: Height of the screen in pixels
            speed_multiplier: Multiplier for cursor movement speed
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed_multiplier = speed_multiplier
        
    def landmark_to_screen(self, landmark: mp.framework.formats.landmark_pb2.NormalizedLandmark) -> Tuple[int, int]:
        """Convert normalized landmark coordinates to screen coordinates.
        
        Args:
            landmark: MediaPipe normalized landmark
            
        Returns:
            Tuple containing screen x and y coordinates
        """
        screen_x = int(landmark.x * self.screen_width * self.speed_multiplier)
        screen_y = int(landmark.y * self.screen_height * self.speed_multiplier)
        
        # Ensure coordinates are within screen bounds
        screen_x = max(0, min(screen_x, self.screen_width))
        screen_y = max(0, min(screen_y, self.screen_height))
        
        return screen_x, screen_y
