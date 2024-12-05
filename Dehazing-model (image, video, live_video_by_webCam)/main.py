import cv2
import numpy as np
from  image_dehazer import image_dehazer # Import the image_dehazer class from your existing code (both mainrun.py and __init__.py must be in same folder)

# Initialize the dehazer
dehazerCamera = image_dehazer(airlightEstimation_windowSze=15, boundaryConstraint_windowSze=3, C0=20, C1=300, regularize_lambda=0.1, sigma=0.5, delta=0.85, showHazeTransmissionMap=False)
dehazerImage = image_dehazer(airlightEstimation_windowSze=15, boundaryConstraint_windowSze=3, C0=20, C1=300, regularize_lambda=0.1, sigma=0.5, delta=0.85, showHazeTransmissionMap=False)

option = int(input("Enter your choice for mode of data:\n 1. Image\n 2. Video\n 3. WebCam\n"))
if option==1:
    path = input("Enter Image path: ")                              # taking user input path
    image_path = path.strip('"').replace('\\', '\\\\')              # Remove the quotes and replace \ with \\
    image = cv2.imread(image_path)                                  # Load the image file
    if image is None:                                               # Check if the image was loaded successfully
        print("Error: Unable to load image. Please check the file path.")
    else:
        dehazed_image, _ = dehazerImage.remove_haze(image)          # Apply the dehazing model to the image
        cv2.imshow('Original Image', image)                         # Display the original images
        cv2.imshow('Dehazed Image', dehazed_image)                  # Display the dehazed images

elif option==2:   
        path = input("Enter Image path: ")
        video_path = path.strip('"').replace('\\', '\\\\')          # Remove the quotes and replace \ with \\
        cap = cv2.VideoCapture(video_path)                          # Load the video file
        while True:
            ret, frame = cap.read()                                 # Read a frame from video file
            if not ret:
                print("Error: Unable to load video. Please check the file path.")
                break
            dehazed_frame, _ = dehazerCamera.remove_haze(frame)     # Apply the dehazing model to the frame
            cv2.imshow('Original Video', frame)                     # Display the original video frame
            cv2.imshow('Dehazed Video', dehazed_frame)              # Display the dehazed video frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

elif option==3:
        cap = cv2.VideoCapture(0)                                   # Open a connection to the webcam
        while True:
            ret, frame = cap.read()                                 # Read a frame from the webcam
            if not ret:
                print("Error: Unable to load video. Please check webCam setting.")
                break
            dehazed_frame, _ = dehazerCamera.remove_haze(frame)     # Apply the dehazing model to the frame
            cv2.imshow('Original Video', frame)                     # Display the original video frame
            cv2.imshow('Dehazed Video', dehazed_frame)              # Display the dehazed video frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

else:
    print("Invalid choice. Please select a valid option (1, 2, or 3).")

# # Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()