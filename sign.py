import os
import cv2

# Ask user for custom labels
label1 = input("Enter label for the first image: ")
label2 = input("Enter label for the second image: ")

# Path to save captured images
IMAGE_PATH = 'CapturedImages'

# Create directory if it doesn't exist
os.makedirs(IMAGE_PATH, exist_ok=True)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera opened correctly
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Function to capture an image and save it
def capture_image(label):
    print(f"Capturing image for label: {label}")
    
    # Wait for the camera to adjust
    input("Press Enter to capture the image...")

    # Capture a frame
    ret, frame = cap.read()
    
    if not ret or frame is None:
        print("Error: Could not read frame from camera.")
        return
    
    # Create image name and save it
    image_name = os.path.join(IMAGE_PATH, f"{label}.jpg")
    if cv2.imwrite(image_name, frame):
        print(f"Image saved: {image_name}")
    else:
        print(f"Error: Could not save image to {image_name}")
    
    # Display the captured image
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(2000)  # Display the image for 2 seconds
    cv2.destroyAllWindows()

# Capture and label two images
capture_image(label1)
capture_image(label2)

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
