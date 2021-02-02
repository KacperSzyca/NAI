import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(3,500) #id 3 = szerokosc
cap.set(4,700) #id 4 = wysokosc

def nothing(x):
    pass


# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('lowH', 'image', 0, 179, nothing)
cv2.createTrackbar('highH', 'image', 14, 179, nothing)

cv2.createTrackbar('lowS', 'image', 25, 255, nothing)
cv2.createTrackbar('highS', 'image', 255, 255, nothing)

cv2.createTrackbar('lowV', 'image', 101, 255, nothing)
cv2.createTrackbar('highV', 'image', 255, 255, nothing)

# https://pysource.com/2018/03/01/find-and-draw-contours-opencv-3-4-with-python-3-tutorial-19/
while (cap.isOpened()):
    success,  img = cap.read()  # czytanie kratek

    blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)



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
    mask = cv2.inRange(img, lower_hsv, higher_hsv)

    contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areaArray = []

    #https://stackoverflow.com/questions/25552765/python-opencv-second-largest-object
    for contour in contours:
            area = cv2.contourArea(contour)
            areaArray.append(area)

    sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

    #cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

    largestContours = []
    if len(sorteddata) > 1:
        for x in range(2):
            largestContours.append(sorteddata[x][1])
            cv2.drawContours(img, sorteddata[x][1], -1, (0, 255, 0), 3)

    cX = []
    cY = []
    minY=[]
    maxY=[]

    #https: // www.pyimagesearch.com / 2016 / 02 / 01 / opencv - center - of - contour /
    if len(sorteddata) > 1:
        for c in range(2):
            # compute the center of the contour
            M = cv2.moments(sorteddata[c][1])
            if M["m10"] > 0 and M["m01"] > 0:
                cX.append(int(M["m10"] / M["m00"]))
                cY.append(int(M["m01"] / M["m00"]))
                x, y, w, h = cv2.boundingRect(sorteddata[1][1])
                minY.append(cY[c]-(h/2))
                maxY.append(cY[c] + (h / 2))



    if len(cY) == 2:
        #sprawdzac gore z dolem
        if ((minY[0] > minY[1] and minY[0] < maxY[1]) or (maxY[0] < maxY[1] and maxY[0] > minY[1])):
            cv2.arrowedLine(img, (cX[0], cY[0]), (cX[1], cY[1]), (0, 255, 255), 2)


    cv2.imshow('image', mask)
    cv2.imshow('frame', img)

    key = cv2.waitKey(1)
    if key == 27:
        break
    key = cv2.waitKey(33)  # https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
    if key == 27:
        break
    elif key == -1:  # normalnie zwraca -1
        continue

cap.release()
cv2.destroyAllWindows()
