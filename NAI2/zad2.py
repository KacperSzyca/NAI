import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
str = open('parameters.txt', 'r').read()
roz = str.split('x');
cap.set(3,int(roz[0])) #id 3 = szerokosc
cap.set(4,int(roz[1])) #id 4 = wysokosc

def nothing(x):
    pass


# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('lowH', 'image', 0, 179, nothing)
cv2.createTrackbar('highH', 'image', 179, 179, nothing)

cv2.createTrackbar('lowS', 'image', 0, 255, nothing)
cv2.createTrackbar('highS', 'image', 255, 255, nothing)

cv2.createTrackbar('lowV', 'image', 0, 255, nothing)
cv2.createTrackbar('highV', 'image', 255, 255, nothing)


while (cap.isOpened()):
    success,  img = cap.read()  # czytanie kratek

    img = cv2.GaussianBlur(img, (21,19),0)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame', hsv)

    # get current positions of the trackbars https://theailearner.com/tag/cv2-inrange-opencv-python/
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])

    # Apply the cv2.inrange method to create a mask
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    # Apply the mask on the image to extract the original color
    frame = cv2.bitwise_and(hsv, hsv, mask=mask)
    cv2.imshow('image', frame)

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        today = datetime.now()
        d4 = today.strftime("%b-%d-%Y_%H-%M-%S")
        d4 = d4 + '.png'
        roi = cv2.selectROI(frame)
        roi_cropped = frame[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]
        cv2.imshow("ROI", roi_cropped)
        cv2.imwrite(d4, roi_cropped)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break