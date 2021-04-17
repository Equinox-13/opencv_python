import cv2

# Import Haarcascade for frontal face
faceCascade = cv2.CascadeClassifier("opencv_python/resources/haarcascade_frontalface_default.xml")
print("check==============>",faceCascade.empty())

img = cv2.imread('opencv_python/resources/elon_musk.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Create a square around face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,128,0), 2)

cv2.imshow("Result",img)
cv2.waitKey(0)