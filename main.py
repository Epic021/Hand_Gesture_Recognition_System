import pickle
import cv2
import mediapipe as mp
import numpy as np


model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']


cap = cv2.VideoCapture(0)


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.7)

# Label dictionary
labels_dict = {0: 'Up', 1: 'Down', 2: 'Left', 3: 'Right', 4: 'Forward', 5: 'Backward', 6: 'Flip', 7: 'Hover', 8: 'Yaw'}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Frame dimensions
    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        # Iterate through detected hands
        for hand_landmarks in results.multi_hand_landmarks:
            x_ = []
            y_ = []
            data_aux = []

            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            
            for landmark in hand_landmarks.landmark:
                x_.append(landmark.x)
                y_.append(landmark.y)

            for landmark in hand_landmarks.landmark:
                data_aux.append(landmark.x - min(x_))
                data_aux.append(landmark.y - min(y_))

            # Bounding box 
            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) + 10
            y2 = int(max(y_) * H) + 10

            # Predict the gesture
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]

            # Display the result on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit with 'Esc' key
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
