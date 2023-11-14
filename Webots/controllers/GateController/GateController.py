from controller import Robot

if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 64
    #previous occurence of the gate being hit
    last_hit = 0.0
          
    #Get and enable Gate device
    gate_sensor = robot.getDevice("GateSensor")
    gate_sensor.enable(timestep)
    
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
    
        #sensor values
        gate_touch = gate_sensor.getValue()
        #time value
        current_time = robot.getTime()  

        #print("Gate_sensor = " + str(gate_sensor.getValue()))
        
        #give some time so initial fall doesn't get recorded
        if gate_touch == 1.0 and (current_time - last_hit) > 2:       
            print("Gate sensor hit at: " + str(current_time))
            
            #print("Last_hit Time: " + str(last_hit))
            #print("Current Time: " + str(current_time))
            
            last_hit = robot.getTime()         
    pass