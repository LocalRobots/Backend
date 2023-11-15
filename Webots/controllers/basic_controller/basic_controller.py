from controller import Robot
from controller import Motor
#import controller
import math


# High level functions
def move_forward(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(max_speed)

def move_back():
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(-max_speed)

def turn_left(): 
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(max_speed)


def turn_right(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(-max_speed)


def drive_forward(angle, inRadians = False): 
    if inRadians: 
        angle *= 57.295   #//180/3.14 = 57
    if angle > 90 or angle < -90:
        pass
    elif angle >= 0:
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity( max_speed * math.sin((angle + 45) / 28.648) )
    else:
        left_motor.setVelocity(max_speed * math.sin((-angle + 45) / 28.648) )
    right_motor.setVelocity(max_speed)

def turn_camera_up():
    camera_motor.setVelocity(-max_camera_speed)

def turn_camera_down():
    camera_motor.setVelocity(max_camera_speed)

def reset_motors():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    camera_motor.setVelocity(0)


if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    
    time_step = 64
    max_speed = .5
    max_camera_speed = 2.0
    
    #All components of the robot
    #left_motor = Motor() 
    #right_motor = Motor() 
    #left_sensor = TouchSensor()
    #right_sensor = TouchSensor() 
    #camera = Camera()
    #camera_motor = Motor()

    #Set up motor/track wheels
    left_motor = robot.getDevice("leftMotor")
    right_motor = robot.getDevice("rightMotor")
    left_motor.setPosition(math.inf)
    right_motor.setPosition(math.inf)

    #Set up touch sensors
    left_sensor = robot.getDevice("left sensor")
    right_sensor = robot.getDevice("right sensor")
    left_sensor.enable(time_step)
    right_sensor.enable(time_step)

    #Set up camera and camera motor
    camera = robot.getDevice("camera")
    camera.enable(time_step)
    camera_motor = robot.getDevice("camera motor")
    camera_motor.setPosition(math.inf)
    camera_motor.setVelocity(0.0)
    reset_motors()

    #Local variables
    width = camera.getWidth()
    height = camera.getWidth()
    
    #Robot AI goes here
    for i in range(0,3):
        move_forward()
        robot.step(time_step * 18)
        reset_motors()
        robot.step(time_step)
        turn_right()
        robot.step(time_step * 18)
        reset_motors()
        robot.step(time_step)

    move_forward()
    robot.step(time_step * 18)
    reset_motors()
    robot.step(time_step)
    turn_left()
    robot.step(time_step * 17)

    for i in range(0,4):
        turn_left()
        robot.step(time_step * 18)
        reset_motors()
        robot.step(time_step)
        move_back()
        robot.step(time_step * 18)
        reset_motors()
        robot.step(time_step)
    
    turn_left()
    robot.step(time_step * 35)
    reset_motors()
    robot.step(time_step)
    
    reset_motors()
    del robot
    pass
