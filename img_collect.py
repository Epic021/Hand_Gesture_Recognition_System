import os
import cv2
import time 

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 9
dataset_size = 300

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print(f"Collecting data for class {j}")

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    half_size = dataset_size // 2
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), f"{counter}.jpg"), frame)

        counter += 1
        # Print when half of the images are stored
        if counter == half_size:
            print(f'Half of the images for class {j} are stored.')
            time.sleep(2)
            print("Switch hands")
            time.sleep(2)


cap.release()
cv2.destroyAllWindows()