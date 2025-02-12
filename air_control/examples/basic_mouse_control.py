"""Basic example of using AirControl for mouse control."""
from air_control import AirControl, AirControlConfig
from air_control.config import MouseConfig

def main():
    # Create custom configuration
    config = AirControlConfig()
    
    # Customize mouse settings
    config.mouse = MouseConfig(
        smoothing_factor=0.5,  # Adjust for smoother/more responsive movement
        speed_multiplier=1.5,  # Adjust for faster/slower cursor movement
        click_threshold=0.025,  # Adjust for more/less sensitive clicks
        fist_detection_threshold=0.6  # Adjust for more/less sensitive drag detection
    )
    
    # Create and run AirControl
    controller = AirControl(config)
    controller.run()

if __name__ == "__main__":
    main()
