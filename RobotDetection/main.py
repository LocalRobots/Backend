import cv2
import numpy as np
from ultralytics import YOLO        

model = YOLO('robotDetection.pt')

def draw_live_arrow(frame, bounding_box):
    #Extract individual values
    x_center, y_center, width, height = bounding_box
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    #Calculate object center 
    object_center_x = x_center 
    object_center_y = y_center 
    #Set robot coordinate
    robot_center_x = frame_width/2
    robot_center_y = frame_height
    # Calculate the endpoint at the middle of the bottom of the object
    object_bottom_middle_x = object_center_x
    object_bottom_middle_y = object_center_y + height / 2 
    # Draw arrow on the image
    line_thickness = 10
    cv2.line(frame, (int(robot_center_x), int(robot_center_y)), (int(object_bottom_middle_x), int(object_bottom_middle_y)), ((209, 255, 189)), line_thickness)
    return frame

# Open camera capture
cap = cv2.VideoCapture(0) #Default camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    names = model.names
    for result in results:
        boxes = result.boxes.cpu().numpy()
        if len(boxes) > 0:
            xyxys = boxes.xyxy
            for c in result.boxes.cls:
                class_names = names[int(c)]
                if class_names == "Balls":
                    #Draw direction to the object 
                    frame_with_arrow = draw_live_arrow(frame, boxes.xywh[int(c)])
            for xyxy in xyxys:
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0,255,0), 2)
                cv2.putText(frame, class_names, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Display the image with the arrow
        cv2.imshow('Direction Arrow', frame_with_arrow)
    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the capture
cv2.release()
cv2.destroyAllWindows()


