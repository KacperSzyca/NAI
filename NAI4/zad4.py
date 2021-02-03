import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(3, 500)  # id 3 = szerokosc
cap.set(4, 700)  # id 4 = wysokosc


def nothing(x):
    pass


# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('lowH', 'image', 0, 179, nothing)
cv2.createTrackbar('lowS', 'image', 25, 255, nothing)
cv2.createTrackbar('lowV', 'image', 101, 255, nothing)
cv2.createTrackbar('highH', 'image', 14, 179, nothing)
cv2.createTrackbar('highS', 'image', 255, 255, nothing)
cv2.createTrackbar('lowV', 'image', 101, 255, nothing)
cv2.createTrackbar('highV', 'image', 255, 255, nothing)

# https://pysource.com/2018/03/01/find-and-draw-contours-opencv-3-4-with-python-3-tutorial-19/
while (cap.isOpened()):
    success, img = cap.read()  # czytanie kratek

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
    #mask = cv2.inRange(img, lower_hsv, higher_hsv)
    # 0 0 0 104 49 255
    #lower_hsv = np.array([0, 0, 0], dtype=np.uint8)
    #higher_hsv = np.array([0, 0, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    contours, hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # https://stackoverflow.com/questions/25552765/python-opencv-second-largest-object
    # https://www.youtube.com/watch?v=mVWQNeY1Pb4
    for contour in contours:
        area = cv2.contourArea(contour)
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) == 4:
            x1, y1, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if (aspectRatio < 0.8 or aspectRatio > 1.2) and float(w) > 80:
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
                # https://madflex.de/find-and-crop-using-opencv/
                # przekazanie całe listy dawało bład
                pst1 = np.float32([approx[1], approx[0], approx[2], approx[3]])
                pst2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
                matrix = cv2.getPerspectiveTransform(pst1, pst2)
                cropped = cv2.warpPerspective(img, matrix, (w, h))
                hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
                #mask1 = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255)) # zielony
                #mask1 = cv2.inRange(hsv, (155, 25, 0), (179, 255, 255))    # czerwony
                mask1 = cv2.inRange(hsv, (25, 52, 72), (102, 255, 255)) # zielony inny
                geryContours, hierachy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for greenContour in geryContours:
                    greenArea = cv2.contourArea(greenContour)
                    greenApprox = cv2.approxPolyDP(greenContour, 0.01 * cv2.arcLength(greenContour, True), True)
                    greenX = greenApprox.ravel()[0]
                    greenY = greenApprox.ravel()[1]
                    #wielkosc koloru zielonego
                    # jak tak to zrobic zdj
                    # metoda prob i bledow
                    if area > 40000:
                        print('Mamy zielone światło!')
                        today = datetime.now()
                        d4 = today.strftime("%b-%d-%Y_%H-%M-%S")
                        d4 = d4 + '.png'
                        corectryRotate = False
                        # obrocic zdj aby zielony to byl prawy dolny rog
                        if ((greenY < h/3) and (greenX < w/3 )):
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                        elif ((greenY < h/3) and (greenX > w/3 )):
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                        elif ((greenY > h/3) and (greenX < w/3 )):
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                            cropped = cv2.rotate(cropped, cv2.cv2.ROTATE_90_CLOCKWISE)
                        cv2.imwrite(d4, cropped)

    try:
        cv2.imshow('out', cropped)
    except NameError:
        print("well, it WASN'T defined after all!")

    cv2.imshow('image', mask)
    cv2.imshow('frame', img)

    key = cv2.waitKey(1)
    if key == 27:
        break
    key = cv2.waitKey(
        33)  # https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
    if key == 27:
        break
    elif key == -1:  # normalnie zwraca -1
        continue

cap.release()
cv2.destroyAllWindows()