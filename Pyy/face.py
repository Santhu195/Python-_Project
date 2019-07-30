import cv2
face_cascade = cv2.CascadeClassifier('hh.xml')

img = cv2.imread('2.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05 , minNeighbors = 5)
print(type(faces))

for x,y,h,w in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
    
#resized = cv2.resize(img, (int(img.shape[1]),(int(img.shape[0]))


cv2.imshow("gray",img)

cv2.waitKey(0)

cv2.destroyAllWindows()