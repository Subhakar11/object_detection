import cv2
import torch
import pyttsx3
import os

# Create a directory to save detected object images
output_dir = 'detected_objects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to speak the detected object
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# def detect_objects(frame):
#     # Perform inference on the frame
#     results = model(frame)
    
#     # Convert the results into a pandas dataframe
#     detections = results.pandas().xyxy[0]  # xyxy format: x1, y1, x2, y2, confidence, class, name
    
#     for index, row in detections.iterrows():
#         # Use only the first 6 values and ignore the rest
#         x1, y1, x2, y2, conf, cls = row[:6]  # Get bounding box and other info

#         # Only consider objects with a confidence level above a certain threshold
#         if conf >= 0.5:  # Set the confidence threshold here
#             # Draw a rectangle on the frame around the detected object
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

#             # Optionally, add the class name and confidence on the frame
#             label = f'{model.names[int(cls)]} {conf:.2f}'
#             cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#             # Speak the detected object
#             speak(model.names[int(cls)])

#             # Save the detected object image
#             object_img = frame[int(y1):int(y2), int(x1):int(x2)]
#             output_path = os.path.join(output_dir, f'detected_{model.names[int(cls)]}_{index}.jpg')
#             cv2.imwrite(output_path, object_img)

#     return frame

def detect_objects(frame):
    results = model(frame)
    
    # Convert the results into a pandas dataframe
    detections = results.pandas().xyxy[0]  # xyxy format: x1, y1, x2, y2, confidence, class, name
    
    conf_threshold = 0.5  # Set a threshold value
    for index, row in detections.iterrows():
        x1, y1, x2, y2, conf, cls = row[:6]  # Get bounding box and other info
        
        # Check if confidence is above threshold
        if conf >= conf_threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            label = f'{model.names[int(cls)]} {conf:.2f}'
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return frame



def start_detection():
    cap = cv2.VideoCapture(0)  # Use the first camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_objects(frame)  # Detect objects in the frame
        cv2.imshow('Detection Feed', frame)  # Show the frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_detection()
