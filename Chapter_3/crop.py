import cv2

img = cv2.imread('opencv_python/resources/cat.jpeg')

# crops an image [height, width]
imgCropped = img[0:150, 150:200]

cv2.imshow("Image Cropped", imgCropped)
cv2.imshow("Image", img)

cv2.waitKey(0)