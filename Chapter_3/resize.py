import cv2

img = cv2.imread('opencv_python/resources/cat.jpeg')

# Retrieves the size of image
# returns (x, y, k) 
# x = height, y = width, k = no. of channels
print(img.shape)

# Resize an image (width, height)
imgResize = cv2.resize(img, (200, 100))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)

cv2.waitKey(0)