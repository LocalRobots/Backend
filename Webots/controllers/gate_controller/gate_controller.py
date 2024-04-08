from controller import Robot

#Script of Robot for Timing Gate, change starting time if needed


if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 64
          
    #Get and enable Gate device
    gate_sensor = robot.getDevice("GateSensor")
    gate_sensor.enable(timestep)
    
    previous_touch = 1.0;
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
    
        #sensor values
        gate_touch = gate_sensor.getValue()
        #time value
        current_time = robot.getTime()  
        
        #print("Gate_sensor = " + str(gate_sensor.getValue()))
        
        #give some time so initial fall doesn't get recorded
        if gate_touch == 1.0 and previous_touch != gate_touch:       
            print("Gate sensor hit at: " + str(current_time))
            #print("Last_hit Time: " + str(last_hit))
            #print("Current Time: " + str(current_time))
        previous_touch = gate_touch
        
    pass