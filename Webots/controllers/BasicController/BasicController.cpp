// File:          BasicController.cpp
// Date:
// Description:
// Author:
// Modifications:

#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/Camera.hpp>
#include <webots/TouchSensor.hpp>

#define TIME_STEP 64
#define MAX_SPEED 2.0

// All the webots classes are defined in the "webots" namespace
using namespace webots;

// This is the main program of your controller.
// It creates an instance of your Robot instance, launches its
// function(s) and destroys it at the end of the execution.
// Note that only one instance of Robot should be created in
// a controller program.
// The arguments of the main function can be specified by the
// "controllerArgs" field of the Robot node
int main(int argc, char** argv) {
    //Create the robot instance.
    Robot* robot = new Robot();

    //Motors/track wheels
    Motor* leftMotor = robot->getMotor("leftMotor");
    Motor* rightMotor = robot->getMotor("rightMotor");
    leftMotor->setPosition(INFINITY);
    rightMotor->setPosition(INFINITY);

    //Touch sensors
    TouchSensor* leftSensor = robot->getTouchSensor("left sensor");
    TouchSensor* rightSensor = robot->getTouchSensor("right sensor");
    leftSensor->enable(TIME_STEP);
    rightSensor->enable(TIME_STEP);

    //Camera
    Camera* camera = robot->getCamera("camera");
    camera->enable(TIME_STEP);
    Motor* cameraMotor = robot->getMotor("camera motor");
    cameraMotor->setPosition(INFINITY);
    //cameraMotor->setTorque(.5);


    //Local variables
    //int turnfullstep = 0;
    //bool turnFull = false;

    //Robot AI
    while (robot->step(TIME_STEP) != -1) {
        //Print any test messages here
        //std::cout << "Hello, World!" << std::endl;

        //Touch sensors are doubles of either 1 or 0
        bool leftSensorActivated = leftSensor->getValue();
        bool rightSensorActivated = leftSensor->getValue();

        /*if (turnFull) {
            //Left
            leftMotor->setVelocity(-MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);
            turnfullstep++;
            if (turnfullstep > 15) {
                turnfullstep = 0;
                turnFull = false;
            }
        }
        else if (leftSensor && rightSensor) {
            turnFull = true;
            //Left
            leftMotor->setVelocity(-MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);
        }
        else */if (leftSensorActivated) {
        //Left
            leftMotor->setVelocity(-MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);
        }
        else if (rightSensorActivated) {
            //Right
            leftMotor->setVelocity(-MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);
        }
        else {
            //Foraward
            leftMotor->setVelocity(MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);;
        }
    }
    delete robot;
    return 0;  // EXIT_SUCCESS
}