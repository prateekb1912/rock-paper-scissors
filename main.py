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
            
            
            # if the index finger tip y coordinate is lower 
            # than the lower part, its "closed"
            if lmList[8][1] > lmList[6][1]:
                print("INDEX FINGER CLOSED")

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow("Rock Paper Scissors", img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()