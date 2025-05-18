# Hand Gesture Recognition System

## Overview
This project is a real-time hand gesture recognition system built using Python, OpenCV, and MediaPipe. It captures hand signs through a live camera feed and can be used for various applications such as drone control, sign language detection, and human-computer interaction.

## Features
- Real-time hand gesture recognition
- Support for 9 different gestures: Up, Down, Left, Right, Forward, Backward, Flip, Hover, and Yaw
- Live camera feed with hand landmark visualization
- Machine learning-based gesture classification using Random Forest
- Real-time gesture prediction display

## Project Structure
- `main.py`: Main application file that handles real-time video capture and gesture recognition
- `model.py`: Contains the machine learning model training code using Random Forest Classifier
- `dataset.py`: Handles dataset creation and management
- `img_collect.py`: Utility for collecting training images
- `voice.py`: Voice feedback integration (optional feature)

## Requirements
- Python
- OpenCV (cv2)
- MediaPipe
- NumPy
- scikit-learn
- Pickle

## Installation
1. Clone the repository
2. Install the required dependencies:
```bash
pip install opencv-python mediapipe numpy scikit-learn
```

## Usage
1. Run the main application:
```bash
python main.py
```
2. Position your hand in front of the camera
3. The system will detect your hand and display the recognized gesture
4. Press 'Esc' to exit the application

## How It Works
1. The system uses MediaPipe to detect hand landmarks in real-time
2. Hand landmarks are processed and normalized
3. The trained Random Forest model predicts the gesture
4. Results are displayed on screen with a bounding box and label

## Training Your Own Model
1. Use `img_collect.py` to collect training data
2. Run `model.py` to train the model
3. The trained model will be saved as 'model.p'

## Notes
- The system requires good lighting conditions for optimal performance
- Hand should be clearly visible in the camera frame
- The model is trained on specific gestures and may need retraining for different gesture sets
