import cv2, time
face_cascade = cv2.CascadeClassifier('hh.xml')
video = cv2.VideoCapture(0)

a= 1

while True:
    a =  a+1
    
    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05 , minNeighbors = 5)
    for x,y,h,w in faces:
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow('capturing', img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break


#print(check)
#print(frame)

#time.sleep(3)





video.release()

cv2.destroyAllWindows()