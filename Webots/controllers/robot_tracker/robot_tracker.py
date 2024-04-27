from controller import Supervisor
from controller import AnsiCodes
import math

# create the Robot instance.
robot = Supervisor()
timestep = int(robot.getBasicTimeStep())
node = robot.getFromDef('Random_0')
stopIfOutside = node.getField('customData').getSFString() != 'true' and node.getField('customData').getSFString() != 'True'

radius = .45
maxError = .075
endAngle = 3.14159265358
moved = False

while robot.step(timestep) != -1:
    
    translation_field = node.getField('translation')
    
    position = node.getPosition()
    magnitude = math.sqrt(pow(position[0], 2) + pow(position[1], 2))
    if stopIfOutside and abs(magnitude - radius) > maxError:
        print(AnsiCodes.YELLOW_FOREGROUND + "Failed: Robot out of bounds..." + AnsiCodes.RESET)#\x1b[33m
        robot.simulationSetMode(0)
        break
    
    #Win condition
    if moved:
        angle = math.atan2(position[1], position[0])
        if angle < 0:
            angle += 2 * math.pi
        if angle > 3.14159265358:
            print(AnsiCodes.GREEN_FOREGROUND + "Gate sensor hit at: " + str(robot.getTime()) + AnsiCodes.RESET)
            robot.simulationSetMode(0)
            break
    elif position[0] > .1 and position[1] > .1:
        moved = True
    
    pass

del robot