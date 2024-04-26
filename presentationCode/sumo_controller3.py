from controller import Robot
from controller import Motor
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

def set_camera_position(rotation):
    camera_motor.setPosition(rotation)
    
def get_camera_position():
    return camera_motor.getTargetPosition()

def reset_motors():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    camera_motor.setVelocity(0)
    
def getCameraColor(camera):
    red = camera.imageGetRed(camera.getImage(), int(width), int(width / 2), int(height / 2))
    green = camera.imageGetGreen(camera.getImage(), int(width), int(width / 2), int(height / 2))
    blue = camera.imageGetBlue(camera.getImage(), int(width), int(width / 2), int(height / 2))
    print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))

#--------------------main function--------------------
if __name__ == "__main__":
    #Create the Robot instance.
    robot = Robot()
    robot.custom_data = 'True'
    speed = 0.3
    #Variables
    time_step = 64
    max_speed = speed
    camera_min_position =  1 #lowest position
    camera_max_position = -1 #highest position
    camera_default_position = 0 #base position
    
    #Set up motor/track wheels
    left_motor = robot.getDevice("leftMotor")
    right_motor = robot.getDevice("rightMotor")
    left_motor.setPosition(math.inf)
    right_motor.setPosition(math.inf)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    
    #Set up camera and camera motor
    camera = robot.getDevice("CameraArm_camera")
    camera.enable(time_step)
    width = camera.getWidth()
    height = camera.getWidth()
    
    #Setting maximum rotational values of camera motor
    camera_motor = robot.getDevice("CameraArm_rotational_motor")
    camera_motor.maxPosition = camera_max_position
    camera_motor.minPosition = camera_min_position


    set_camera_position(0.1)
    robot.step(time_step*3)
    #Main Loop while simulation is running
    while robot.step(time_step) != -1:
        #Code goes here
        max_speed = speed
        #RGB Values for debugging center pixel
        red = camera.imageGetRed(camera.getImage(), int(width), int(width / 2), int(height / 2))
        green = camera.imageGetGreen(camera.getImage(), int(width), int(width / 2), int(height / 2))
        blue = camera.imageGetBlue(camera.getImage(), int(width), int(width / 2), int(height / 2))
        print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
        
        if blue > 200 or red > 170:
            set_camera_position(.65)
            robot.step(time_step*3)
        while blue > 50:
            red = camera.imageGetRed(camera.getImage(), int(width), int(width / 2), int(height / 2))
            green = camera.imageGetGreen(camera.getImage(), int(width), int(width / 2), int(height / 2))
            blue = camera.imageGetBlue(camera.getImage(), int(width), int(width / 2), int(height / 2))
            print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
            move_forward()
            robot.step(time_step)
            if red < 40 or (60 <= red and red <= 75):
                print("found border")
                move_back()
                robot.step(time_step)
                max_speed = 0.025
                turn_right()
                robot.step(time_step*7)
                set_camera_position(0.1)
                robot.step(time_step*8)
                                                
                red = camera.imageGetRed(camera.getImage(), int(width), int(width / 2), int(height / 2))
                green = camera.imageGetGreen(camera.getImage(), int(width), int(width / 2), int(height / 2))
                blue = camera.imageGetBlue(camera.getImage(), int(width), int(width / 2), int(height / 2))
                print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
                while red >= 70 and green > 100 or red < 40:
                    red = camera.imageGetRed(camera.getImage(), int(width), int(width / 2), int(height / 2))
                    green = camera.imageGetGreen(camera.getImage(), int(width), int(width / 2), int(height / 2))
                    blue = camera.imageGetBlue(camera.getImage(), int(width), int(width / 2), int(height / 2))
                    print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))

                    if red < 90 and green < 131: #or red < 200 and green < 165:
                        print("found object")
                        max_speed = 0.5
                        set_camera_position(0.65)
                        robot.step(time_step)
                        max_speed = speed
                        break
                    else:
                        turn_right()
                        robot.step(time_step)
                set_camera_position(.65)
                robot.step(time_step*4)
    
        pass #end of code region
                
    #End of AI
    reset_motors()
    del robot
    pass  # EXIT_SUCCESS
