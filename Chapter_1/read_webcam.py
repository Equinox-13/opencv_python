import cv2

# Reads webcam stream 0 for the default cam subsequent no. for using other cams
cap = cv2.VideoCapture(0)

# Sets width of screen with id 3
cap.set(3, 640)
# Sets height of screen with id 4
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

   