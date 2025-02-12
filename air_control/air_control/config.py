"""Configuration management for AirControl."""
from dataclasses import dataclass
from typing import Optional

@dataclass
class HandTrackingConfig:
    """Configuration for hand tracking parameters."""
    static_image_mode: bool = False
    max_num_hands: int = 1
    min_detection_confidence: float = 0.65
    min_tracking_confidence: float = 0.65

@dataclass
class MouseConfig:
    """Configuration for mouse control parameters."""
    smoothing_factor: float = 0.5
    speed_multiplier: float = 1.5
    click_threshold: float = 0.025
    fist_detection_threshold: float = 0.6

@dataclass
class CameraConfig:
    """Configuration for camera parameters."""
    camera_id: int = 0
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[int] = None

@dataclass
class AirControlConfig:
    """Main configuration class for AirControl."""
    hand_tracking: HandTrackingConfig = HandTrackingConfig()
    mouse: MouseConfig = MouseConfig()
    camera: CameraConfig = CameraConfig()
