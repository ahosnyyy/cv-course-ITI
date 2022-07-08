import cv2


def rescale_frame(in_frame, scale=0.75):
    width = int(in_frame.shape[1] * scale)
    height = int(in_frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(in_frame, dimensions, interpolation=cv2.INTER_AREA)


img = cv2.imread('../resources/images/cat.jpg')
img_resized = rescale_frame(img)
cv2.imshow('Cat', img)
cv2.imshow('Cat Resized', img_resized)
cv2.waitKey(0)

# Reading Videos
capture = cv2.VideoCapture('../resources/videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)

    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
    if isTrue:
        cv2.imshow('Video', frame)
        cv2.imshow('Video Resized', frame_resized)
        if cv2.waitKey(20) & 0xFF == ord('c'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()



