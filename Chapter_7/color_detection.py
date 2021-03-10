import cv2

img = cv2.imread('opencv_python/resources/lambo.jpeg')

img = cv2.resize(img, (600, 400))

# Convert image to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("HSV Image", imgHSV)
cv2.waitKey(0)