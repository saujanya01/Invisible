import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(60):
    ret,background = cap.read()

background=np.flip(background,axis=1)

while(cap.isOpened()):
    ret,img = cap.read()
    img = np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([101,50,38])
    upper_blue = np.array([110,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask=cv2.bitwise_not(mask)
    inter_image=cv2.bitwise_and(img,img,mask=mask)
    inter_image0 = cv2.bitwise_and(background, background, mask = mask)
    final_output = cv2.addWeighted(inter_image,1,inter_image0,1,0)
    cv2.imshow("final",final_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    
cap.release()
cv2.destroyAllWindows()