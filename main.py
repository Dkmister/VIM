import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    negative = 255 - frame

    mirror_x = cv2.flip(frame,1)

    mirror_y = cv2.flip(frame,0)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    canny = cv2.Canny(frame,100,200)

    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)

    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    
    # Display the resulting frame
    cv2.imshow('gray',gray)
    cv2.imshow('rgb',frame)
    cv2.imshow('canny',canny)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('negative',negative)
    cv2.imshow('flip x',mirror_x)
    cv2.imshow('flip y',mirror_y)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
