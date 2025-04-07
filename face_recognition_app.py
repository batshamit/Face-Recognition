import cv2
import face_detect
import face_recognition
import numpy as np
import sqlite3
import os

# Database Connection
with sqlite3.connect("face_database.db") as conn:
    cursor = conn.cursor()

    known_faces = []
    known_names = []

    # Fetch names and image paths from the database
    cursor.execute("SELECT name, image_path FROM users")
    for row in cursor.fetchall():
        name, image_path = row
        if not os.path.exists(image_path):
            print(f"⚠️ Warning: Image not found for {name} at {image_path}")
            continue

        image = face_detect.load_image_file(image_path)
        encodings = face_detect.face_encodings(image)

        if encodings:  # Ensure encoding is found
            known_faces.append(encodings[0])
            known_names.append(name)
        else:
            print(f"⚠️ Warning: No face found in {image_path}")

# Start Camera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("⚠️ Warning: Failed to capture frame from camera.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    # Detect Faces
    face_locations = face_detect.face_locations(rgb_frame)
    face_encodings = face_detect.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        distances = face_detect.face_distance(known_faces, face_encoding)
        min_distance_index = np.argmin(distances) if len(distances) > 0 else None

        name = "Unknown"
        details = ""

        if min_distance_index is not None and distances[min_distance_index] < 0.6:
            name = known_names[min_distance_index]

            # Fetch Details from Database
            cursor.execute("SELECT * FROM users WHERE name=?", (name,))
            user_data = cursor.fetchone()
            if user_data:
                details = f"Name: {user_data[1]}, Age: {user_data[2]}, Address: {user_data[3]}"

        # Display Box & Name on Screen
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, details, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Face Recognition System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
video_capture.release()
cv2.destroyAllWindows()
