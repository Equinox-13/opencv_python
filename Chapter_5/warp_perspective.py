import cv2
import numpy as np

img = cv2.imread('opencv_python/resources/cards.jpeg')

width, height = 250, 350

# Contains x,y axis of the 4 points
pts1 = np.float32([[531,101], [733,146], [478,374], [681,418]])

# output image 4 points
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])

# warp perspective
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
