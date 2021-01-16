import cv2

# file path of image
path = 'opencv_python/resources/cat.jpeg'

# Reads image
img = cv2.imread(path)

# Display image in a window
cv2.imshow("Output",img)

# Halts image window
cv2.waitKey(0)