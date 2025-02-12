"""Camera handling functionality."""
from typing import Optional, Tuple

import cv2
import numpy as np

from ..config import CameraConfig

class Camera:
    """Handles video capture and frame processing."""
    
    def __init__(self, config: CameraConfig):
        """Initialize the camera.
        
        Args:
            config: Configuration for camera settings
        """
        self.config = config
        self.cap = cv2.VideoCapture(config.camera_id)
        
        if config.width:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.width)
        if config.height:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.height)
        if config.fps:
            self.cap.set(cv2.CAP_PROP_FPS, config.fps)
            
    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Read a frame from the camera.
        
        Returns:
            Tuple containing:
                - Boolean indicating if frame was successfully read
                - Frame data if successful, None otherwise
        """
        success, frame = self.cap.read()
        if not success:
            return False, None
        return True, frame
    
    def release(self) -> None:
        """Release the camera resource."""
        self.cap.release()
