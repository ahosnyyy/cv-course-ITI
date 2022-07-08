import cv2
img = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)

# Reading Videos
capture = cv2.VideoCapture('../resources/videos/kitten.mp4')  # 0 from webcam

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('c'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv2.imshow('Video', frame)
        if cv2.waitKey(20) & 0xFF == ord('c'):
            break            
    else:
        break

capture.release()
cv2.destroyAllWindows()

