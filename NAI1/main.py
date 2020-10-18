import cv2


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("Resources/video.mp4")
cap.set(3,640) #id 3 = szerokosc
cap.set(4,480) #id 4 = wysokosc

while True:
    success,  img = cap.read()  # czytanie kratek
    imgMirroring = cv2.flip(img,1) # odbicie lustrzane
    cv2.imshow("Normalne",img)
    cv2.imshow("Odbite", imgMirroring)
    key = cv2.waitKey(33) # https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
    if key==27:
        break
    elif key==-1: # normalnie zwraca -1
        continue




