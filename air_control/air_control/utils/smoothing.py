"""Movement smoothing utilities."""
from typing import Tuple

class MovementSmoother:
    """Handles smoothing of movement coordinates."""
    
    def __init__(self, smoothing_factor: float = 0.5):
        """Initialize the movement smoother.
        
        Args:
            smoothing_factor: Factor for movement smoothing (0-1)
        """
        self.smoothing_factor = smoothing_factor
        self.last_x = 0
        self.last_y = 0
        
    def smooth(self, current_x: float, current_y: float) -> Tuple[float, float]:
        """Apply smoothing to current coordinates.
        
        Args:
            current_x: Current x coordinate
            current_y: Current y coordinate
            
        Returns:
            Tuple containing smoothed x and y coordinates
        """
        smooth_x = (1 - self.smoothing_factor) * current_x + self.smoothing_factor * self.last_x
        smooth_y = (1 - self.smoothing_factor) * current_y + self.smoothing_factor * self.last_y
        
        self.last_x = smooth_x
        self.last_y = smooth_y
        
        return smooth_x, smooth_y
