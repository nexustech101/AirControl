import cv2
import mediapipe as mp
import pyautogui
import numpy as np


class HandTrackingMouseController:
    def __init__(self, smoothing_factor=0.5, speed_multiplier=1.5):
        """
        Initialize the hand tracking mouse controller.

        :param smoothing_factor: Controls the smoothness of mouse movement (0-1)
        :param speed_multiplier: Multiplies mouse movement speed
        """
        # MediaPipe and OpenCV setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.65
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.INTEGRATED_WEB_CAM = 0
        self.EXTERNAL_WEB_CAM = 1

        # Screen and movement parameters
        self.screen_width, self.screen_height = pyautogui.size()
        self.smoothing_factor = smoothing_factor
        self.speed_multiplier = speed_multiplier

        # Tracking variables
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.dragging = False
        self.last_action = None

        # Gesture sensitivity
        self.click_threshold = 0.025
        self.fist_detection_threshold = 0.6

    def _smooth_mouse_movement(self, current_x, current_y):
        """
        Apply smoothing to mouse movement.

        :param current_x: Current x coordinate
        :param current_y: Current y coordinate
        :return: Smoothed x, y coordinates
        """
        smooth_x = (1 - self.smoothing_factor) * current_x + \
            self.smoothing_factor * self.last_mouse_x
        smooth_y = (1 - self.smoothing_factor) * current_y + \
            self.smoothing_factor * self.last_mouse_y

        return smooth_x, smooth_y

    def _calculate_screen_coordinates(self, hand_landmarks, frame_shape):
        """
        Convert hand landmark coordinates to screen coordinates.

        :param hand_landmarks: MediaPipe hand landmarks
        :param frame_shape: Shape of the video frame
        :return: Scaled and accelerated screen coordinates
        """
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

        # Convert to screen coordinates
        screen_x = int(index_tip.x * self.screen_width)
        screen_y = int(index_tip.y * self.screen_height)

        # Apply speed multiplier
        screen_x = int(screen_x * self.speed_multiplier)
        screen_y = int(screen_y * self.speed_multiplier)

        # Ensure coordinates are within screen bounds
        screen_x = max(0, min(screen_x, self.screen_width))
        screen_y = max(0, min(screen_y, self.screen_height))

        return screen_x, screen_y

    def detect_click_gesture(self, hand_landmarks):
        """
        Detect click gesture by measuring distance between index finger and thumb.

        :param hand_landmarks: MediaPipe hand landmarks
        :return: Tuple of (left_click, right_click)
        """
        index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

        index_distance = np.sqrt(
            (index_tip.x - thumb_tip.x) ** 2 +
            (index_tip.y - thumb_tip.y) ** 2
        )

        pinky_distance = np.sqrt(
            (pinky_tip.x - thumb_tip.x) ** 2 +
            (pinky_tip.y - thumb_tip.y) ** 2
        )

        return (index_distance < self.click_threshold,
                pinky_distance < self.click_threshold)

    def detect_fist(self, hand_landmarks):
        """
        Detect if hand is in a fist position.

        :param hand_landmarks: MediaPipe hand landmarks
        :return: Boolean indicating fist detection
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

        # Check if all finger tips are below their base
        return all(
            hand_landmarks.landmark[tip].y > hand_landmarks.landmark[base].y
            for tip, base in zip(finger_tips, finger_bases)
        )

    def detect_fingertips_touching(self, hand_landmarks):
        """
        Detect if all fingertips are touching or very close together.

        :param hand_landmarks: MediaPipe hand landmarks
        :return: Boolean indicating fingertips are touching
        """
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP,
            self.mp_hands.HandLandmark.THUMB_TIP
        ]

        # Calculate distances between all fingertips
        tip_distances = []
        for i in range(len(finger_tips)):
            for j in range(i+1, len(finger_tips)):
                tip1 = hand_landmarks.landmark[finger_tips[i]]
                tip2 = hand_landmarks.landmark[finger_tips[j]]

                distance = np.sqrt(
                    (tip1.x - tip2.x) ** 2 +
                    (tip1.y - tip2.y) ** 2
                )
                tip_distances.append(distance)

        # Check if all fingertips are very close to each other
        touch_threshold = 0.5  # Adjust this value to fine-tune touch sensitivity
        return all(distance < touch_threshold for distance in tip_distances)

    def process_hand_control(self, frame):
        """
        Main method to process hand tracking and mouse control.

        :param frame: Video frame from webcam
        :return: Processed frame
        """
        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)
        pyautogui.FAILSAFE = False

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Calculate screen coordinates with smoothing and acceleration
                screen_x, screen_y = self._calculate_screen_coordinates(hand_landmarks, frame.shape)
                smooth_x, smooth_y = self._smooth_mouse_movement(screen_x, screen_y)

                # Detect gestures
                left_click, right_click = self.detect_click_gesture(hand_landmarks)
                is_fist = self.detect_fist(hand_landmarks)
                # is_all_fingertips = self.detect_fingertips_touching(hand_landmarks)

                # Perform mouse actions
                if left_click:
                    pyautogui.click()
                elif right_click:
                    pyautogui.rightClick()

                # Dragging logic
                if is_fist:
                    if not self.dragging:
                        pyautogui.mouseDown(smooth_x, smooth_y)
                        self.dragging = True
                    pyautogui.moveTo(smooth_x, smooth_y)
                else:
                    pyautogui.mouseUp()
                    self.dragging = False

                # Always move mouse
                pyautogui.moveTo(smooth_x, smooth_y)

                # Update last mouse position
                self.last_mouse_x, self.last_mouse_y = smooth_x, smooth_y

                # Optionally draw hand landmarks
                self.mp_drawing.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def run(self):
        """
        Main method to run hand tracking mouse control.
        """
        # Open webcam
        cap = cv2.VideoCapture(self.INTEGRATED_WEB_CAM)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Flip frame for mirror effect
            frame = cv2.flip(frame, 1)

            # Process hand control
            frame = self.process_hand_control(frame)

            # Display frame
            cv2.imshow("Hand Tracking Mouse Control", frame)

            # Exit on 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Cleanup
        cap.release()
        cv2.destroyAllWindows()


# Example usage
if __name__ == "__main__":
    controller = HandTrackingMouseController(
        smoothing_factor=0.01,  # Smoothing factor for mouse movements
        speed_multiplier=1.5   # Speed factor for mouse movements
    )
    controller.run()
