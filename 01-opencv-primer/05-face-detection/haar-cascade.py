import cv2

cap_marvel = cv2.imread('../resources/faces/capmarvel.jpg')
cap_gray = cv2.cvtColor(cap_marvel, cv2.COLOR_BGR2GRAY)
cv2.imshow('Captin Marvel ', cap_gray)
cv2.waitKey(0)

# Load Cascade filter
face_cascade = cv2.CascadeClassifier('../resources/haarcascade_frontalface_default.xml')


# Create the face detecting function
def detect_face(img):
    img_copy = img.copy()
    face_rects = face_cascade.detectMultiScale(img_copy, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 255, 255), 3)

    return img_copy


# Detect the face
face_detected = detect_face(cap_gray)
cv2.imshow('Face', face_detected)
cv2.waitKey(0)

# Load the image file and convert the color mode
avengers = cv2.imread('../resources/faces/avengers.jpg')
avengers = cv2.cvtColor(avengers, cv2.COLOR_BGR2GRAY)
# Detect the face and plot the result
detected_avengers = detect_face(avengers)
cv2.imshow('Avengers', detected_avengers)
cv2.waitKey(0)

