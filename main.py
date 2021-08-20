import cv2
import mediapipe as mp
from HandDetectorModule.tracker import HandDetector
import time

cap = cv2.VideoCapture(0)
cv2.namedWindow("Rock Paper Scissors")

pTime = time.time()

detector = HandDetector()

# The indices for the tips of the fingers on hand
TIP_IDS = [4, 8, 12, 16, 20]


while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)

        img = detector.findHands(img)

        # Get all landmarks from the detected hand
        lmList = detector.findPosition(img)

        if len(lmList) > 0:
            
            fingers = []

            # For the thumb, we will use a different logic,
            # we will check if the tip is left or right of the lower part
            if lmList[TIP_IDS[4]][0] < lmList[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # if the finger tips' y coordinate is lower 
            # than the lower part, its "closed"
            for id in range(1,5):
                if lmList[TIP_IDS[id]][1] < lmList[TIP_IDS[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            print(fingers)


        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow("Rock Paper Scissors", img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()