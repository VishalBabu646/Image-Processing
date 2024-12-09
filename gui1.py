import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import math

# Function to run a python script
def run_script(script_name):
    try:
        result = subprocess.run(["python", script_name], check=True, capture_output=True, text=True)
        print(result.stdout)  # Print the output of the script
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to run {script_name}: {e}\n{e.stderr}")

# Function to change button color on hover
def on_enter(event):
    event.widget.config(bg='lightblue')

def on_leave(event):
    event.widget.config(bg='green')

# Function to draw a flower on the canvas
def draw_flower(canvas, x_offset):
    petal_color = "purple"
    petal_length = 30
    petal_width = 15

    # Draw petals using ovals
    for i in range(6):  # Draw 6 petals
        angle = i * 60  # 60 degrees apart
        x = x_offset + petal_length * math.cos(math.radians(angle))
        y = 50 + petal_length * math.sin(math.radians(angle))
        canvas.create_oval(x - petal_width, y - petal_length, x + petal_width, y, fill=petal_color, outline=petal_color)

    # Draw the flower center
    canvas.create_oval(x_offset - 20, 50 - 20, x_offset + 20, 50 + 20, fill='yellow', outline='yellow')

    # Repeat the flower vertically
    for j in range(1, 8):  # Repeat flowers down the canvas
        y_offset = j * 80  # Adjust space between flowers
        canvas.create_oval(x_offset - 20, y_offset - 20, x_offset + 20, y_offset + 20, fill='yellow', outline='yellow')
        for i in range(6):  # Draw 6 petals for each flower
            angle = i * 60  # 60 degrees apart
            x = x_offset + petal_length * math.cos(math.radians(angle))
            y = y_offset + petal_length * math.sin(math.radians(angle))
            canvas.create_oval(x - petal_width, y - petal_length, x + petal_width, y, fill=petal_color, outline=petal_color)

# Initialize the main window
root = tk.Tk()
root.title("Driver Fatigue Detection System Using Thermal and RBG Images")

# Set the window size
root.geometry("800x400")  # Adjusted size for better layout

# Add a title label
title_label = tk.Label(root, text="Driver Fatigue Detection System Using Thermal and RBG Images", font=("Helvetica", 20))  # Increased font size
title_label.pack(pady=20)

# Create left and right design canvases for flowers
left_canvas = tk.Canvas(root, bg='lightgray', width=200, height=400)  # Increased width to 200
left_canvas.pack(side=tk.LEFT, fill=tk.Y)  # Left canvas
draw_flower(left_canvas, 100)  # Center the flower in the canvas

right_canvas = tk.Canvas(root, bg='lightgray', width=200, height=400)  # Increased width to 200
right_canvas.pack(side=tk.RIGHT, fill=tk.Y)  # Right canvas
draw_flower(right_canvas, 100)  # Center the flower in the canvas

# Load and display an image below the title
try:
    image = Image.open("Image-Driver_Fatigue.png")  # Ensure 'Image-Driver_Fatigue.png' is in the same directory
    image = image.resize((300, 300), Image.LANCZOS)  # Increased size to 300x300
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=image_tk)
    image_label.pack(pady=10)
except Exception as e:
    messagebox.showwarning("Warning", f"Could not load image: {e}")

# Create a frame to hold the buttons horizontally
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons for each script
scripts = ["Real_Time_RBG.py", "Real_Time_Thermal.py", "RBG_&_Themal_Image.py"]  # Added .py extension
for script in scripts:
    button = tk.Button(button_frame, text=script, command=lambda s=script: run_script(s), font=("Helvetica", 12), bg='green')
    button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)  # Pack buttons horizontally and expand to fill space
    button.bind("<Enter>", on_enter)  # Bind hover event to change color
    button.bind("<Leave>", on_leave)   # Bind leave event to change color back

# Start the main event loop
root.mainloop()
