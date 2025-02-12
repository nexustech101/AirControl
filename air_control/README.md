# AirControl | Hand Gesture Mouse Control

AirControl is a sophisticated Python package that enables intuitive mouse control through hand gestures using computer vision technology. Built with modularity and extensibility in mind, it provides a robust framework for implementing hand gesture controls that can be integrated into various applications, from gaming to presentation tools.

## 🌟 Key Features

### Core Functionality
- **Advanced Hand Tracking**: Utilizes MediaPipe's hand tracking technology for accurate gesture recognition
- **Precise Mouse Control**: Smooth cursor movement with configurable sensitivity and acceleration
- **Multiple Gesture Support**: Built-in support for various gestures:
  - Index finger movement for cursor control
  - Thumb-index pinch for left-click
  - Thumb-pinky pinch for right-click
  - Fist gesture for drag operations
- **Real-time Processing**: Efficient frame processing for responsive control

### Technical Features
- **Modular Architecture**: Clean separation of concerns for easy maintenance and extension
- **Configurable Components**: Flexible configuration system for all components
- **Custom Gesture Support**: Extensible gesture system for adding new controls
- **Smooth Movement**: Advanced movement smoothing algorithm for precise control
- **Error Handling**: Robust error handling and graceful degradation

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Webcam or camera device
- Windows, macOS, or Linux operating system

### Steps
1. Clone the repository:
```bash
git clone https://github.com/nexustech101/AirControl.git
cd AirControl
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### Basic Usage
```python
from air_control import AirControl

# Create and run with default settings
controller = AirControl()
controller.run()
```

### Custom Configuration
```python
from air_control import AirControl, AirControlConfig
from air_control.config import MouseConfig, CameraConfig

# Create custom configuration
config = AirControlConfig()

# Customize mouse settings
config.mouse = MouseConfig(
    smoothing_factor=0.5,     # Higher = smoother but more latency
    speed_multiplier=1.5,     # Adjust cursor speed
    click_threshold=0.025,    # Adjust click sensitivity
    fist_detection_threshold=0.6  # Adjust drag sensitivity
)

# Customize camera settings
config.camera = CameraConfig(
    camera_id=0,  # Change for different camera
    width=1280,   # Custom resolution
    height=720,
    fps=30
)

# Create controller with custom config
controller = AirControl(config)
controller.run()
```

## 🏗️ Project Structure

```
air_control/
├── air_control/
│   ├── core/               # Core functionality
│   │   ├── camera.py      # Camera handling
│   │   ├── hand_tracker.py # Hand tracking
│   │   └── mouse.py       # Mouse control
│   ├── gestures/          # Gesture implementations
│   │   ├── base.py        # Base gesture classes
│   │   ├── click.py       # Click gestures
│   │   └── drag.py        # Drag gestures
│   ├── utils/             # Utility functions
│   │   ├── coordinates.py # Coordinate transformation
│   │   └── smoothing.py   # Movement smoothing
│   ├── config.py          # Configuration management
│   └── __init__.py        # Package initialization
├── examples/              # Example applications
├── tests/                # Test cases
├── requirements.txt      # Dependencies
└── setup.py             # Package setup
```

## 🔧 Advanced Usage

### Creating Custom Gestures
```python
from air_control.gestures.base import BaseGesture
import mediapipe as mp

class CustomGesture(BaseGesture):
    def __init__(self, threshold: float = 0.1):
        super().__init__()
        self.threshold = threshold
    
    def detect(self, hand_landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> bool:
        # Implement custom gesture detection logic
        return True  # or False based on detection
```

### Integrating with Games
```python
from air_control import AirControl
import pygame  # or any other game library

class GameController:
    def __init__(self):
        self.air_control = AirControl()
        
    def process_gestures(self, game_state):
        # Customize gesture handling for your game
        hand_landmarks = self.air_control.hand_tracker.get_landmarks()
        if hand_landmarks:
            # Map gestures to game actions
            pass
```

## 🎮 Example Applications

1. **Basic Mouse Control** (`examples/basic_mouse_control.py`):
   - Standard mouse control implementation
   - Configurable settings example

2. **Custom Gestures** (`examples/custom_gestures.py`):
   - Implementation of custom gesture detection
   - Example of extending base gesture class

## 🔍 Troubleshooting

### Common Issues
1. **Poor Detection**
   - Ensure good lighting conditions
   - Keep hand within camera frame
   - Adjust camera position and angle

2. **Laggy Movement**
   - Reduce smoothing_factor in configuration
   - Check system performance
   - Ensure camera FPS is adequate

3. **Gesture Recognition Issues**
   - Adjust gesture thresholds in configuration
   - Ensure clear hand visibility
   - Check for background interference

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests if applicable
5. Submit a pull request

Please ensure your code follows our coding standards and includes appropriate documentation.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MediaPipe team for their excellent hand tracking solution
- OpenCV community for computer vision tools
- PyAutoGUI developers for mouse control capabilities

## 📞 Support

For issues and feature requests, please use the GitHub issue tracker.

---

Built with ❤️ by nexustech101
