import tkinter as tk
import subprocess
from PIL import Image, ImageTk  # Import Pillow

def start_realtime_monitoring():
    # Run the realtime.py script
    subprocess.Popen(['python', 'realtime_demo.py'])

# Create the main window
root = tk.Tk()
root.title("Driver Fatigue Detection")

# Load and resize the image
image_path = "Image-Driver_Fatigue.png"  # Change this to your image file name
image = Image.open(image_path)

# Resize the image (e.g., to 200x200 pixels)
image = image.resize((200, 200), Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=1, padx=10, pady=10)  # Move image to the right

# Create a label for the title
title_label = tk.Label(root, text="Driver Fatigue Detection Using RGB and Thermal Images", font=("Helvetica", 16))
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Align to the left

# Create a prompt text label
prompt_label = tk.Label(root, text="Click here to start real-time monitoring", font=("Helvetica", 12))
prompt_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Align to the left

# Create a button to start real-time monitoring
start_button = tk.Button(root, text="Start Monitoring", command=start_realtime_monitoring, height=2, width=20)
start_button.grid(row=2, column=0, padx=10, pady=20)  # Center the button

# Run the Tkinter event loop
root.mainloop()
