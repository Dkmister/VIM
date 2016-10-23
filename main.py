import numpy as np
import copy
import cv2

def nothing(y):
    pass

cv2.namedWindow("Original Window", cv2.WINDOW_NORMAL)
cv2.namedWindow('Transformed Window', cv2.WINDOW_NORMAL)

# Trackbars
flipBrightnessLevel = 'Brightness'
cv2.createTrackbar(flipBrightnessLevel, 'Original Window',0,255,nothing)

flipConstrastLevel = 'Constrast'
cv2.createTrackbar(flipConstrastLevel,'Original Window',0,255,nothing)

flipGaussianBlurLevel = 'GaussianBlur'
cv2.createTrackbar(flipGaussianBlurLevel, 'Original Window',0,255,nothing)

# Flags
gaussianBlurActive = False
cannyActive = False
sobelActive = False 
brightnessActive = False
constrastActive = False
negativeActive = False
grayscaleActive = False
resizeActive = False
rotateActive = False
xFlipActive = False
yFlipActive = False

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
    resultFrame = copy.deepcopy(frame)
else:
    rval = False

fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out = cv2.VideoWriter('result.avi', fourcc, 20.0, (frame.shape[1],frame.shape[0]))

while rval:
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False 

    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord('q'):
		if gaussianBlurActive == True:
			gaussianBlurActive = False
		else:
			gaussianBlurActive = True
    if key == ord('w'):
        if cannyActive == True:
	    cannyActive = False
	else:
	    cannyActive = True
    if key == ord('e'):
	if sobelActive == True:
	    sobelActive = False
        else:
            sobelActive = True
    if key == ord('r'):
	if brightnessActive == True:
	    brightnessActive = False
	else:
	    brightnessActive = True
    if key == ord('t'):
	if contrastActive == True:
	    contrastActive = False
	else:
	    contrastActive = True
    if key == ord('y'):
	if negativeActive == True:
	    negativeActive = False
	else:
	    negativeActive = True
    if key == ord('u'):
	if grayscaleActive == True:
       	    grayscaleActive = False
	else:
	    grayscaleActive = True
    if key == ord('i'):
	if resizeActive == True:
	    resizeActive = False
        else:
	    resizeActive = True
    if key == ord('o'):
	if rotateActive == True:
	    rotateActive = False
	else:
	    rotateActive = True
    if key == ord('p'):
	if xFlipActive == True:
	    xFlipActive = False
	else:
	    xFlipActive = True
    if key == ord('a'):
	if yFlipActive == True:
	    yFlipActive = False
	else:
	    yFlipActive = True
	
   cv2.imshow('Original Video', frame)

	
   resultFrame = copy.deepcopy(frame)

    if gaussianBlurActive:
        kSize = cv2.getTrackbarPos(flipGaussianBlurLevel,'Original Video')
	if kSize % 2 == 0:
	    kSize-=1
	resultFrame = copy.deepcopy(cv2.GaussianBlur(frame,(kSize,kSize),30))
    if cannyActive:
	resultFrame = copy.deepcopy(cv2.Canny(frame,100,200))
    if sobelActive:
	resultFrame = copy.deepcopy(cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5))
    if brightnessActive:
	amount = cv2.getTrackbarPos(flipBrightnessLevel,'Original Video')
	resultFrame = cv2.add(frame, np.full((frame.shape[0],frame.shape[1],3), amount, np.uint8))
    if contrastActive:
	amount = cv2.getTrackbarPos(flipContrastLevel,'Original Video')
	resultFrame = cv2.multiply(frame, np.full((frame.shape[0],frame.shape[1],3), amount, np.uint8))
    if negativeActive:
        negative = 255 - frame
	resultFrame = negative
    if grayscaleActive:
	resultFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if resizeActive:
	resultFrame = cv2.resize(frame,((frame.shape[0])/2,(frame.shape[1])/2))
    if rotateActive:
	rows=frame.shape[0]
	cols=frame.shape[1]
	resultFrame = cv2.warpAffine(frame, cv2.getRotationMatrix2D((cols/2,rows/2),90,1),(cols,rows))
    if xFlipActive:
	resultFrame = cv2.flip(frame,1)
    if yFlipActive:
	resultFrame = cv2.flip(frame,0)

    cv2.imshow('Result Video',resultFrame)
    out.write(resultFrame)

vc.release()
out.release()
cv2.destroyWindow('Original Video')
cv2.destroyWindow('Result Video')
    
# Capture frame-by-frame
#    ret, frame = cap.read()
#    rows = frame.shape[0]
#    cols = frame.shape[1]
#    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
#    rotated = cv2.warpAffine(frame,M,(cols,rows))
#   negative = 255 - frame
#  mirror_x = cv2.flip(frame,1)
# mirror_y = cv2.flip(frame,0)
#blur = cv2.GaussianBlur(frame,(15,15),0)

# Our operations on the frame come here
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
#canny = cv2.Canny(frame,100,200)
#sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
#sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    
    # Display the resulting frame
