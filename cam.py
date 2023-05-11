import cv2
from random import randrange

# Face classifier
trained_face_data = cv2.CascadeClassifier("Algorithms/face.xml")

webcam = cv2.VideoCapture(0)

print("Press q to quit.")

while True:
    sucessful_frame_read, frame = webcam.read()

    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)),10)

    cv2.imshow('Face detector', frame)

    key = cv2.waitKey(1)

    if key == 81 or key==113:
        break

print("Code completed.")