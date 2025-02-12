"""Mouse control functionality."""
from typing import Tuple

import pyautogui

from ..config import MouseConfig
from ..utils.smoothing import MovementSmoother

class MouseController:
    """Handles mouse movement and actions."""
    
    def __init__(self, config: MouseConfig):
        """Initialize the mouse controller.
        
        Args:
            config: Configuration for mouse control
        """
        self.config = config
        self.smoother = MovementSmoother(config.smoothing_factor)
        self.screen_width, self.screen_height = pyautogui.size()
        self.dragging = False
        pyautogui.FAILSAFE = False
        
    def move(self, x: float, y: float) -> None:
        """Move mouse to specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        smooth_x, smooth_y = self.smoother.smooth(x, y)
        pyautogui.moveTo(smooth_x, smooth_y)
        
    def click(self, right: bool = False) -> None:
        """Perform mouse click.
        
        Args:
            right: If True, perform right click instead of left click
        """
        if right:
            pyautogui.rightClick()
        else:
            pyautogui.click()
            
    def start_drag(self, x: float, y: float) -> None:
        """Start dragging from specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        if not self.dragging:
            smooth_x, smooth_y = self.smoother.smooth(x, y)
            pyautogui.mouseDown(smooth_x, smooth_y)
            self.dragging = True
            
    def end_drag(self) -> None:
        """End dragging operation."""
        if self.dragging:
            pyautogui.mouseUp()
            self.dragging = False
            
    def get_screen_dimensions(self) -> Tuple[int, int]:
        """Get screen dimensions.
        
        Returns:
            Tuple containing screen width and height
        """
        return self.screen_width, self.screen_height
