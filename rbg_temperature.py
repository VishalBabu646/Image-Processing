import cv2
import dlib
import numpy as np
from imutils import face_utils
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Eye aspect ratio to detect blink
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Function to determine fatigue
def determine_fatigue(ear, blink_count, consecutive_frames, ear_threshold, consecutive_frames_threshold):
    if ear < ear_threshold:
        consecutive_frames += 1
        if consecutive_frames >= consecutive_frames_threshold:
            return "Fatigue Detected", blink_count, consecutive_frames
    else:
        if consecutive_frames >= consecutive_frames_threshold:
            blink_count += 1
        consecutive_frames = 0
    
    return "No Fatigue Detected", blink_count, consecutive_frames

# Function to process the image for blink detection
def process_image(image_path, ear_threshold=0.25, consecutive_frames_threshold=3):
    # Load the pre-trained dlib face detector
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("Error", "Could not load the image.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    blink_count = 0
    consecutive_frames = 0
    fatigue_status = "No Fatigue Detected"

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]]
        rightEye = shape[face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        fatigue_status, blink_count, consecutive_frames = determine_fatigue(
            ear, blink_count, consecutive_frames, ear_threshold, consecutive_frames_threshold
        )

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)

        cv2.putText(image, f"Status: {fatigue_status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(image, f"Blinks: {blink_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Convert image to RGB for displaying in Tkinter
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# Function to open file dialog and select an image for processing
def open_file_for_processing():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        result_image = process_image(file_path)
        if result_image is not None:
            display_image(result_image)

# Function to display the processed image in the GUI
def display_image(image):
    # Convert image to PIL format
    img = Image.fromarray(image)
    img = img.resize((400, 400), Image.LANCZOS)  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    
    # Display the image
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

# Initialize the main window
root = tk.Tk()
root.title("Driver Fatigue Detection Using RGB Image")
root.geometry("600x600")

# Add a title label
title_label = tk.Label(root, text="Driver Fatigue Detection Using RGB Image", font=("Helvetica", 16))
title_label.pack(pady=20)

# Label to display the processed image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Button to select an image
select_image_button = tk.Button(root, text="Select Image", command=open_file_for_processing, font=("Helvetica", 12), width=25)
select_image_button.pack(pady=20)

# Run the main event loop
root.mainloop()
