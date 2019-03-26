import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(60):
    ret, background = cap.read()
    background = np.flip(background, axis = 1)

cv2.imshow("Background",background)
while True:
    _, frame = cap.read()
    frame = np.flip(frame, axis = 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower1 = np.array([90,50,50])
    upper1 = np.array([150,255,255])
    mask = cv2.inRange(hsv,lower1,upper1)
    
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)
    n_closing = np.bitwise_not(closing)

    
    res_c = cv2.bitwise_and(background, background, mask = closing)
    res = cv2.bitwise_and(frame,frame,mask = n_closing)
    final = cv2.addWeighted(res,1,res_c,1,0)
    cv2.imshow("frame",frame)
    cv2.imshow("closing",closing)
    cv2.imshow("res_c",res_c)
    cv2.imshow("res",res)
    cv2.imshow("final",final)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.imshow("background",background)
cv2.destroyAllWindows()