import cv2


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("resources/video.mp4")
cap.set(3,300) #id 3 = szerokosc
cap.set(4,300) #id 4 = wysokosc
frame_counter = 0
while (cap.isOpened()):
    success,  img = cap.read()  # czytanie kratek
    frame_counter += 1
    #If the last frame is reached, reset the capture and the frame_counter
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 #Or whatever as long as it is the same as next line
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    imgMirroring = cv2.flip(img,1) # odbicie lustrzane
    cv2.imshow("Normalne",img)
    cv2.imshow("Odbite", imgMirroring)
    key = cv2.waitKey(33) # https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
    if key==27:
        break
    elif key==-1: # normalnie zwraca -1
        continue




