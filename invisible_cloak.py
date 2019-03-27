import cv2
import numpy as np

def nothing(x):
    return(x)

cap = cv2.VideoCapture(0)

for i in range(60):
    ret, background = cap.read()
    background = np.flip(background, axis = 1)

cv2.imshow("Background",background)
while True:
    _, frame = cap.read()
    frame = np.flip(frame, axis = 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",hsv)
    
    cv2.namedWindow('HSV min')
    cv2.createTrackbar('H minimum','HSV min',0,180,nothing)
    cv2.createTrackbar('S minimum','HSV min',0,255,nothing)
    cv2.createTrackbar('V minimum','HSV min',0,255,nothing)
    
    cv2.namedWindow('HSV max')
    cv2.createTrackbar('H maximum','HSV max',0,180,nothing)
    cv2.createTrackbar('S maximum','HSV max',0,255,nothing)
    cv2.createTrackbar('V maximum','HSV max',0,255,nothing)

    h_min = cv2.getTrackbarPos('H minimum','HSV min')
    s_min = cv2.getTrackbarPos('S minimum','HSV min')
    v_min = cv2.getTrackbarPos('V minimum','HSV min')
    
    h_max = cv2.getTrackbarPos('H maximum','HSV max')
    s_max = cv2.getTrackbarPos('S maximum','HSV max')
    v_max = cv2.getTrackbarPos('V maximum','HSV max')
    
    lower1 = np.array([h_min,s_min,v_min])
    upper1 = np.array([h_max,s_max,v_max])
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
    
cap.release()
cv2.imshow("background",background)
cv2.destroyAllWindows()