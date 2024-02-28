import cv2 as cv    

#capture video
capture = cv.VideoCapture(0)
#process frame by frame for thresholding
while True:
    istrue, frame = capture.read()
    cv.imshow('Video', frame)
    #turn image to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #thresholding
    thresholding, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    cv.imshow('Simple Thresholded', thresh)
    
    #destroy loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)
