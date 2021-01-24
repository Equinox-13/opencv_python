import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# Puts text on image
cv2.putText(img, " OPENCV ", (240,256), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 150, 0), 3)
cv2.putText(img, " Python ", (200,180), cv2.FONT_HERSHEY_PLAIN, 2, (0, 150, 0), 3)

cv2.imshow("Text on image", img)

cv2.waitKey(0)