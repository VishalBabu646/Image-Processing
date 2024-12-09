import cv2
import numpy as np

# Function to calculate the average temperature in a given region
def average_temperature(thermal_image, mask):
    return cv2.mean(thermal_image, mask=mask)[0]

# Load thermal camera feed
cap = cv2.VideoCapture(0)  # Change to the correct index for your thermal camera

# Define masks for regions of interest
# Example masks for the eyes, forehead, and nasal area (these need to be defined based on your camera's resolution)
eye_mask = np.zeros((480, 640), dtype=np.uint8)  # Example dimensions; adjust as needed
forehead_mask = np.zeros((480, 640), dtype=np.uint8)
nose_mask = np.zeros((480, 640), dtype=np.uint8)

# Manually set regions in masks (for example purposes, these coordinates are arbitrary)
cv2.rectangle(eye_mask, (200, 150), (300, 200), 255, -1)  # Adjust coordinates for eyes
cv2.rectangle(forehead_mask, (200, 50), (300, 100), 255, -1)  # Adjust coordinates for forehead
cv2.rectangle(nose_mask, (230, 120), (270, 140), 255, -1)  # Adjust coordinates for nose

while True:
    ret, frame = cap.read()  # Read frame from thermal camera
    if not ret:
        break
    
    # Assuming frame is already a thermal image; if not, convert it accordingly

    # Calculate average temperatures for the regions of interest
    eye_temp = average_temperature(frame, eye_mask)
    forehead_temp = average_temperature(frame, forehead_mask)
    nose_temp = average_temperature(frame, nose_mask)

    # Determine fatigue based on temperature readings
    # You can adjust the thresholds based on experimental data
    fatigue_detected = False
    if eye_temp > 35.0:  # Example threshold for eyes
        fatigue_detected = True
    if forehead_temp < 32.0:  # Example threshold for forehead
        fatigue_detected = True
    if nose_temp < 33.0:  # Example threshold for nose
        fatigue_detected = True

    # Display the results
    cv2.putText(frame, f"Eye Temp: {eye_temp:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.putText(frame, f"Forehead Temp: {forehead_temp:.1f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.putText(frame, f"Nose Temp: {nose_temp:.1f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    if fatigue_detected:
        cv2.putText(frame, "Fatigue Detected!", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

    cv2.imshow("Thermal Image", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
