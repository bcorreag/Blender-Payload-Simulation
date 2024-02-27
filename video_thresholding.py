import cv2 as cv    

#img = cv.imread('test_img.png')

#cv.imshow('Payload', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Gray', gray)

# # Simple Thresholding
# thresholding, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

# cv.imshow('Simple Thresholded', thresh)


capture = cv.VideoCapture(0)
while True:
    istrue, frame = capture.read()
    cv.imshow('Video', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    thresholding, thresh = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)
    cv.imshow('Simple Thresholded', thresh)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)