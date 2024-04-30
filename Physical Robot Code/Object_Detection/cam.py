import cv2
from picamera2 import Picamera2, Preview
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np


picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()


preview_config['main']['size'] = (640, 480)
preview_config['main']['format'] = "RGB888"


picam2.configure(preview_config)
picam2.start()


model = YOLO('yolov8n.pt')


file_path = '/home/pibot/rpi-bookworm-yolov8-main/coco.txt'
try:
    with open(file_path, "r") as my_file:
        class_list = my_file.read().split("\n")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit(1)

count = 0
while True:
    im = picam2.capture_array()

    count += 1
    if count % 3 != 0:
        continue
    im = cv2.flip(im, 1)
    results = model.predict(im)
    px = pd.DataFrame(results[0].boxes.data).astype("float")

    for index, row in px.iterrows():
        x1, y1, x2, y2, d = int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[5])
        c = class_list[d]

        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cvzone.putTextRect(im, f'{c}', (x1, y1), 1, 1)
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
