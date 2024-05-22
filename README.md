# Volume Control using Hand Gestures

## Overview
This project enables you to control the system volume using hand gestures captured by your webcam. The index finger and thumb are used as key points to manipulate the volume level.

## Libraries and Tools
- **OpenCV**: For accessing the webcam and processing images.
- **Mediapipe**: For hand detection and tracking.
- **pycaw**: For controlling the system volume.

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Required Modules
Install the required modules using pip:

```sh
pip install opencv-python mediapipe numpy pycaw
```

## Usage
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the script using Python:

```sh
python VolumeHandControl.py
```

### How it Works
- The script captures video feed from the webcam.
- Mediapipe processes the video to detect hands and marks the key points on them.
- The distance between the index finger and thumb is calculated to adjust the volume.

## Project Structure
- **VolumeHandControl.py**: Main script to run the volume control functionality.

## Detailed Steps

1. **Import Libraries**:
   ```python
   import cv2
   import mediapipe as mp
   import time
   from ctypes import cast, POINTER
   from comtypes import CLSCTX_ALL
   from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
   ```

2. **Hand Detection Class**:
   - Initialize Mediapipe Hands and Drawing utilities.
   - Detect hands and find positions of key landmarks.

3. **Volume Control Logic**:
   - Calculate the distance between the index finger and thumb.
   - Map the distance to a volume range and set the system volume accordingly.

4. **Main Loop**:
   - Capture video from the webcam.
   - Use the hand detection class to find hand landmarks.
   - Adjust the volume based on the distance between key landmarks.
   - Display the video feed with landmarks and volume level.

## Example Output
The script displays a video feed with the detected hand landmarks. The current volume level is displayed on the screen, and it changes as you move your index finger and thumb closer or further apart.

## Troubleshooting
- Ensure your webcam is properly connected.
- Make sure all required Python packages are installed.
- If the hand detection is not working, check the Mediapipe documentation for troubleshooting tips.

## Acknowledgements
- [Mediapipe](https://github.com/google/mediapipe)
- [OpenCV](https://opencv.org/)
- [pycaw](https://github.com/AndreMiras/pycaw)

## Contact
For any questions or suggestions, please contact [Divya Sirala] at [divya.sirala@gmail.com].
