import RPi.GPIO as GPIO
from time import sleep
import sys
import tty
import termios
import subprocess
import threading

# Motor 1 Pins
in1_1 = 31
in2_1 = 29

# Motor 2 Pins
in1_2 = 33
in2_2 = 32

servo_pin = 37

GPIO.setmode(GPIO.BOARD)

# Setup Motor 1
GPIO.setup(in1_1, GPIO.OUT)
GPIO.setup(in2_1, GPIO.OUT)

# Setup Motor 2
GPIO.setup(in1_2, GPIO.OUT)
GPIO.setup(in2_2, GPIO.OUT)

# Function to capture video
def capture_video():
    subprocess.run(["rpicam-vid", "-t", "100000", "-o", "test.h264"])

# Function to get a single character from stdin
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Function to stop both motors
def stop_motors():
    GPIO.output(in1_1, GPIO.LOW)
    GPIO.output(in2_1, GPIO.LOW)
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)

# Function to move both motors forward
def forward():
    GPIO.output(in1_1, GPIO.HIGH)
    GPIO.output(in2_1, GPIO.LOW)
    GPIO.output(in1_2, GPIO.HIGH)
    GPIO.output(in2_2, GPIO.LOW)

# Function to move both motors backward
def backward():
    GPIO.output(in1_1, GPIO.LOW)
    GPIO.output(in2_1, GPIO.HIGH)
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.HIGH)

# Function to turn left
def turn_left():
    GPIO.output(in1_1, GPIO.LOW)
    GPIO.output(in2_1, GPIO.HIGH)
    GPIO.output(in1_2, GPIO.HIGH)
    GPIO.output(in2_2, GPIO.LOW)

# Function to turn right
def turn_right():
    GPIO.output(in1_1, GPIO.HIGH)
    GPIO.output(in2_1, GPIO.LOW)
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.HIGH)


try:
    # Start video capture thread
    video_thread = threading.Thread(target=capture_video)
    video_thread.start()

    # Main loop to control the robot
    while True:
        char = getch()
        if char == 'w':
            forward()
        elif char == 's':
            backward()
        elif char == 'a':
            turn_left()
        elif char == 'd':
            turn_right()
        elif char == 'q':
            stop_motors()
            break 

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    stop_motors()
    GPIO.cleanup()
