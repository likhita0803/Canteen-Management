import cv2

# Load the pre-trained face detector from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam or video capture device (in this case, using the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Enhance contrast in the frame (optional)
    # You can adjust the parameters according to your needs
    gray = cv2.equalizeHist(gray)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    # Check the number of detected faces
    num_faces = len(faces)

    # If more than one face detected, print "INVALID FACE"
    if num_faces > 1:
        message = "INVALID FACE"
        text_color = (0, 0, 255)  # Red color for text
    elif num_faces == 1:
        message = "It is a face"
        text_color = (0, 255, 0)  # Green color for text
    else:
        message = "NOT A FACE"
        text_color = (0, 0, 255)  # Red color for text

    # Loop over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display text on the frame based on the message
        cv2.putText(frame, message, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    # Display the text on the frame
    cv2.putText(frame, message, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Display the frame with face detection
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
