import cv2
import numpy as np

# Create a blank image 0 means black with 3 levels
img = np.zeros((512, 512, 3), np.uint8)
print(img)

#  Below is used to color a specific part [height:height,width:width]
# img[200:300, 100:300] = 255,0,0

# Just a colon is used to color whole image
img[:] = 255,0,0

cv2.imshow("Image", img)
cv2.waitKey(0)
