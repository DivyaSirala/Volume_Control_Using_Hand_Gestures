import cv2
import time
import numpy as np
import HandTrackingModule as HTM
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


############ Parameters #########
wCam, hCam = 640, 480
#################################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

#accuracy in deteection by increasing detection confidence
detector = HTM.handDetector(detectionCon=0.7)

#Computer Volume control using pycaw library
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#checking the volumne, it ranges from -65.0(min) to 0(max)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        # printing value of a particular points, tipf of thumb and tip of index
        # these values can be found in mediapipe official page
        #    print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        #finding middle of the line and calulating a circle at its middle
        cx, cy = (x1+x2)//2, (y1+y2)//2

        #creating circles on those given points
        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
        #creating lines between the points
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255),3)

        #Calulating length to decide the volumne range using math module
        length = math.hypot(x2-x1, y2-y1)
        print(length)
        #Hand range 50 to 300
        #volume range -65.5 to 0
        #Converting the hand range to volume range using numpy
        vol = np.interp(length, [20,250], [minVol, maxVol])
        volBar = np.interp(length, [20,250], [400, 150])
        volPer = np.interp(length, [20,250], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        #Getting maximum and min from the line by making it a center circle
        if length<50:
            cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)

    # printing the volume bar in the corner with % value
    cv2.rectangle(img, (20,150), (85,400), (0,255,0), 3)
    cv2.rectangle(img, (20,int(volBar)), (85,400), (0,255,0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%' , (40,450), cv2.FONT_HERSHEY_PLAIN,
                1, (0,255,0), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS : {int(fps)}', (40,70), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,0,0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)

