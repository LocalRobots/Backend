import RPi.GPIO as GPIO
import cv2
from picamera2 import Picamera2, Preview
from ultralytics import YOLO
import cvzone
import numpy as np
import pandas as pd
import subprocess
import threading
import sys
import tty
import termios
from time import sleep

# Motor Pins Setup
in1_1 = 31
in2_1 = 29
in1_2 = 33
in2_2 = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup([in1_1, in2_1, in1_2, in2_2], GPIO.OUT)

# Initialize Picamera2
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
preview_config['main']['size'] = (640, 480)
preview_config['main']['format'] = "RGB888"
picam2.configure(preview_config)
picam2.start()

# Load YOLO model
model = YOLO('yolov8n.pt')

# Read class labels from file
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

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def stop_motors():
    GPIO.output([in1_1, in2_1, in1_2, in2_2], GPIO.LOW)

def control_motors(char):
    if char == 'w':
        GPIO.output([in1_1, in1_2], GPIO.HIGH)
        GPIO.output([in2_1, in2_2], GPIO.LOW)
    elif char == 's':
        GPIO.output([in1_1, in1_2], GPIO.LOW)
        GPIO.output([in2_1, in2_2], GPIO.HIGH)
    elif char == 'a':
        GPIO.output([in1_1, in2_2], GPIO.LOW)
        GPIO.output([in2_1, in1_2], GPIO.HIGH)
    elif char == 'd':
        GPIO.output([in1_1, in2_2], GPIO.HIGH)
        GPIO.output([in2_1, in1_2], GPIO.LOW)
    elif char == 'q':
        stop_motors()
        return True
    return False

count = 0
try:
    while True:
        char = getch()
        if control_motors(char):
            break

        im = picam2.capture_array()
        count += 1
        if count % 3 != 0:
            continue
        im = cv2.flip(im, -1)
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
finally:
    GPIO.cleanup()
    cv2.destroyAllWindows()
    picam2.stop()
