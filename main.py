import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

cv2.namedWindow("Rock Paper Scissors", cv2.WINDOW_KEEPRATIO)

while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)
        cv2.imshow("Rock Paper Scissors", img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()