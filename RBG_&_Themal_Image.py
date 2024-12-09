import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps

# Function to calculate mean temperature from thermal image
def calculate_temperature(image_path):
    # Load the thermal image in RGB format
    image = cv2.imread(image_path)

    if image is None:
        messagebox.showerror("Error", "Image not loaded. Check the file path.")
        return None, None

    # Temperature scaling values (adjust based on your data)
    min_temp = 20  # minimum temperature the camera can measure
    max_temp = 40  # maximum temperature the camera can measure

    # Assuming the temperature data is in the red channel (or modify according to your data)
    red_channel = image[:, :, 2]  # Extract the red channel

    # Normalize the red channel to the temperature range
    temperature_map = min_temp + (red_channel / 255.0) * (max_temp - min_temp)

    # Define regions of interest (ROI) for eyes and forehead (adjust coordinates as needed)
    eye_roi = temperature_map[30:50, 40:60]  # Example coordinates for eye region
    forehead_roi = temperature_map[10:30, 40:60]  # Example coordinates for forehead region

    mean_eye_temp = np.mean(eye_roi)
    mean_forehead_temp = np.mean(forehead_roi)

    return mean_eye_temp, mean_forehead_temp

# Function to determine fatigue based on temperatures
def determine_fatigue(mean_eye_temp, mean_forehead_temp):
    threshold = 1.0  # Define a temperature difference threshold (example value)
    temp_difference = abs(mean_eye_temp - mean_forehead_temp)
    
    if temp_difference > threshold:
        return "Fatigue Detected"
    else:
        return "No Fatigue Detected"

# Function to open file dialog and select image for mean temperature calculation
def open_file_for_temperature():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if file_path:
        mean_eye_temp, mean_forehead_temp = calculate_temperature(file_path)
        if mean_eye_temp is not None and mean_forehead_temp is not None:
            fatigue_status = determine_fatigue(mean_eye_temp, mean_forehead_temp)
            result_label.config(text=f"Mean eye temperature: {mean_eye_temp:.2f}°C\n"
                                     f"Mean forehead temperature: {mean_forehead_temp:.2f}°C\n"
                                     f"Status: {fatigue_status}")
            # Load image into the GUI
            load_image(file_path)

# Function to display selected image in the GUI
def load_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.Resampling.LANCZOS)  # Resize for display in the GUI
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep reference to avoid garbage collection

# Initialize the main window
root = tk.Tk()
root.title("Driver Fatigue Detection System Using Thermal and RGB Images")
root.geometry("600x700")

# Add a title label
title_label = tk.Label(root, text="Driver Fatigue Detection System Using Thermal and RGB Images", font=("Helvetica", 16))
title_label.pack(pady=20)

# Load and display an image
try:
    image = Image.open("image.png")  # Ensure 'image.png' is in the same directory
    image = image.resize((150, 150), Image.Resampling.LANCZOS)
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=image_tk)
    image_label.pack(pady=10)
except Exception as e:
    messagebox.showwarning("Warning", f"Could not load image: {e}")

# Button to select image
select_image_button = tk.Button(root, text="Select Image", command=open_file_for_temperature, font=("Helvetica", 12), width=25)
select_image_button.pack(pady=5)

# Label to display result
result_label = tk.Label(root, text="Mean eye temperature: \nMean forehead temperature: \nStatus: ", font=("Arial", 14))
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
