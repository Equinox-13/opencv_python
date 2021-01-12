import cv2

# Reads video file
cap = cv2.VideoCapture('/home/bista/practice/opencv_projects/opencv_python/resources/sample_video.mp4')

# Video is basically a set of images so looping through it.
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    # Checks for key press q if True then breaks
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
