

import cv2
import dlib
import face_recognition
from tkinter import *
from PIL import Image, ImageTk
import os
import shutil

# Directory to store user images and data
user_data_directory = "user_data"

# Load the Dlib facial landmark predictor
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Function to capture and save a new user's photo
def capture_and_save_user(username, root):
    # Create the user data directory if it doesn't exist
    if not os.path.exists(user_data_directory):
        os.makedirs(user_data_directory)

    # Read a frame from the video stream
    ret, frame = cap.read()

    # Save the captured photo
    user_image_path = os.path.join(user_data_directory, f"{username}.jpg")
    cv2.imwrite(user_image_path, frame)
    print(f"Photo captured and saved for user: {username}")

    # Update the model (you need to implement this part)
    # ...

    # Display the captured image
    image = Image.open(user_image_path)
    image = image.resize((300, 300), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(image=image)
    image_label.imgtk = imgtk
    image_label.configure(image=imgtk)

    # Destroy the capture window after a delay
    root.after(2000, lambda: root.destroy())

# Function to recognize and log in a user
def recognize_user():
    # Load known user data
    known_user_encodings = []
    known_user_names = []

    for file in os.listdir(user_data_directory):
        if file.endswith(".jpg"):
            username = os.path.splitext(file)[0]
            user_image_path = os.path.join(user_data_directory, file)
            image = face_recognition.load_image_file(user_image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_user_encodings.append(encoding)
            known_user_names.append(username)

    # Initialize dlib face detector
    detector = dlib.get_frontal_face_detector()

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame to RGB for face_recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Use dlib to detect faces
        faces = detector(rgb_frame)

        # Convert the dlib face object to rectangle coordinates
        face_locations = [(face.top(), face.right(), face.bottom(), face.left()) for face in faces]

        # Find face encodings
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Check if any faces are detected
        if face_locations:
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_user_encodings, face_encoding)

                # Display the name of the recognized user if a match is found
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_user_names[first_match_index]

                # Draw a rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Display the name on the frame
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            # Display the frame with face recognition
            cv2.imshow('Face Recognition', frame)

            # Ask for user feedback
            user_feedback = input("Is the recognized name correct? (y/n): ")

            # If the user provides feedback, update the model
            if user_feedback.lower() == 'n':
                correct_name = input("Enter the correct name: ")
                # Implement the model update logic here (e.g., retraining the model)
                # ...

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()

# Function to clear all data in the user_data_directory
def clear_data():
    confirmation = input("Are you sure you want to clear all data? (y/n): ")
    if confirmation.lower() == 'y':
        shutil.rmtree(user_data_directory)
        print("All data cleared.")
    else:
        print("Data clearing aborted.")

# Main loop
while True:
    print("Select an option:")
    print("1. New User")
    print("2. Login")
    print("3. Clear Data")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        new_username = input("Enter the name of the new user: ")

        # Create a new window for capturing and saving a new user's photo
        root = Tk()
        root.title("Capture User Photo")

        # Display the video stream
        video_label = Label(root)
        video_label.pack()

        # Create a label for displaying the captured image
        image_label = Label(root)
        image_label.pack()

        # Call the capture_and_save_user function with the new username and root window
        capture_and_save_user(new_username, root)

        # Run the Tkinter main loop
        root.mainloop()
    elif choice == '2':
        recognize_user()
    elif choice == '3':
        clear_data()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")