import cv2
import numpy as np

def analyze_fatigue(frame):
    """Analyze the thermal frame for signs of fatigue."""
    # Convert the color image to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate the mean temperature (pixel intensity in grayscale)
    mean_temp = np.mean(gray_frame)
    fatigue_threshold = mean_temp + 5  # Adjust based on baseline data

    # Create a mask for areas above the fatigue threshold
    fatigue_mask = gray_frame > fatigue_threshold

    return mean_temp, fatigue_mask, gray_frame

def main(camera_index=0):
    """Main function to capture video from the thermal camera and analyze it."""
    cap = cv2.VideoCapture(camera_index)  # Change index if needed

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Analyze the frame for fatigue
        mean_temp, fatigue_mask, gray_frame = analyze_fatigue(frame)

        # Determine fatigue status
        fatigue_status = "Fatigued" if np.any(fatigue_mask) else "Not Fatigued"

        # Display results
        cv2.putText(frame, f'Mean Temperature: {mean_temp:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Status: {fatigue_status}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if fatigue_status == "Fatigued" else (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('Thermal Image', frame)
        cv2.imshow('Grayscale Image', gray_frame)
        cv2.imshow('Fatigue Detection Mask', (fatigue_mask.astype(np.uint8) * 255))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    main()
