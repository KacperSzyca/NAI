import cv2

#https://drive.google.com/drive/folders/1cQXRv5lLxG3JoGd3KsBwIFb3QyIXdoma
cap = cv2.VideoCapture('bikes.mp4')

# https://www.youtube.com/watch?v=IrsZCtlDOjk

# https://drive.google.com/drive/folders/1tgaUtp8pdycv0Sw5H87cDpFhdBLl8veJ
cascade = cv2.CascadeClassifier('twoWheels.xml')

count = 0
while True:
    ret, img = cap.read()

    height, width = img.shape[0:2]

    ##blur = cv2.blur(img,(3,3))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bikes = cascade.detectMultiScale(gray, 1.1)

    cv2.line(img, (0, height - 200), (width, height-200), (0, 255, 0), 3)

    matches = []
    for (x, y, w, h) in bikes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

        bikeCy=int(y+h/2)
        lineCy=height-200

        #margines 16 px, naliczane w momencie najechania na linie
        if(bikeCy<lineCy+8 and bikeCy>lineCy-8):
            count += 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "bike", (x, y), cv2.QT_FONT_NORMAL, 1, (0, 0, 0), 2)




    cv2.putText(img, "Count: " + str(count), (width-170, height-10), cv2.FONT_ITALIC, 1, (0, 0, 0), 2)
    cv2.imshow('live', img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()