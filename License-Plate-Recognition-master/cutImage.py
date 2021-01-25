import cv2
import time
# cap = cv2.VideoCapture('D:\video.mp4')
cap = cv2.VideoCapture(0)
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i > 10:
        break
    time.sleep(1)
    cv2.imwrite(str(i) +'.jpg',frame)
    i=i+1

cap.release()
cv2.destroyAllWindows()

