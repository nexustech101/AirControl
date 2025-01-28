# AirControl | Hand Tracking Mouse Controller

Control your mouse cursor and perform click, drag, and other actions using hand gestures tracked by your webcam. This project leverages **OpenCV**, **MediaPipe**, and **PyAutoGUI** to create an intuitive, touchless interface for interacting with your computer.

---

## Features
- **Hand Gesture Recognition**: Detects hand gestures for cursor control, left-click, right-click, and dragging.
- **Smooth Mouse Movements**: Uses a smoothing algorithm for precise control.
- **Gesture-Based Clicks**: Perform left-click or right-click with specific finger gestures.
- **Fist Detection for Dragging**: Enables drag-and-drop actions by closing your fist.
- **Customizable Parameters**: Adjust sensitivity, smoothing, and speed to suit your needs.

---

## Demo
![Hand Tracking Demo](demo.gif)
- Coming soon...

---

## Technologies Used
- **Python**: Core programming language.
- **OpenCV**: For webcam video input and image processing.
- **MediaPipe**: For hand tracking and landmark detection.
- **PyAutoGUI**: To control mouse events like moving, clicking, and dragging.
- **NumPy**: For efficient mathematical operations.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nexustech101/AirControl.git
    cd AirControl
    ```

2. Optionally create a virtual environment:
- Windows
    ```bash
    python -m venv venv
    ```
- MAC OS
    ```bash
    python -m venv venv
    ```
- Linux
    ```bash
    python3 -m venv venv
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:
    ```bash
    python main.py
    ```

---

## Usage

1. Ensure you have a functional webcam connected to your system.
2. Run the program to open the webcam interface.
3. Use the following gestures:
    - **Cursor Movement**: Move your index finger.
    - **Left Click**: Pinch the index finger and thumb.
    - **Right Click**: Pinch the pinky finger and thumb.
    - **Drag and Drop**: Close your fist and move your hand.
4. Press `q` to exit the program.

---

## Configuration

Customize the behavior of the controller by modifying parameters in the script:
- `smoothing_factor`: Controls the smoothness of mouse movements (`0.0` for instant movement, `1.0` for maximum smoothing).
- `speed_multiplier`: Adjusts the cursor speed.
- `click_threshold`: Sensitivity for detecting clicks.
- `fist_detection_threshold`: Sensitivity for detecting fist gestures.

---

## Limitations

- Works best with good lighting conditions.
- May struggle with detecting gestures when hands are too close to or far from the webcam.
- Gesture detection might vary depending on background and hand positioning.

---

## Future Enhancements

- Add support for multi-hand tracking.
- Enable custom gesture mapping for specific actions.
- Implement scrolling functionality using hand gestures.
- Enhance accuracy for low-light environments.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [MediaPipe by Google](https://mediapipe.dev/) for the hand tracking solution.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for simulating mouse movements.
- [OpenCV](https://opencv.org/) for image processing.
- Inspired by the endless possibilities of computer vision.

---

## Contact

If you have questions, suggestions, or feedback, feel free to open an issue or contact me directly.
