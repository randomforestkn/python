import cv2
import numpy as np

capture = cv2.VideoCapture('test.avi')

if (capture.isOpened() == False):
    print("Error with opening.")

while(capture.isOpened()):

    ret, frame = capture.read()
    if ret == True:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
cv2.destroyAllWindows()
