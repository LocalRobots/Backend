// File:          trackController.cpp
// Date:
// Description:
// Author:
// Modifications:

// You may need to add webots include files such as
// <webots/DistanceSensor.hpp>, <webots/Motor.hpp>, etc.
// and/or to add some other includes
#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/DistanceSensor.hpp>

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
    // create the Robot instance.
    //console.writeline("Using Controller);

    Robot* robot = new Robot();

    Motor* leftMotor, * rightMotor;
    DistanceSensor* dsl = robot->getDistanceSensor("left distance sensor");
    DistanceSensor* dsr = robot->getDistanceSensor("right distance sensor");
    leftMotor = robot->getMotor("leftMotor");
    rightMotor = robot->getMotor("rightMotor");
    leftMotor->setPosition(INFINITY);
    rightMotor->setPosition(INFINITY);
    leftMotor->setVelocity(0.1);
    rightMotor->setVelocity(0.1);
    dsl->enable(TIME_STEP);
    dsr->enable(TIME_STEP);

    //int turnfullstep = 0;
    //bool turnFull = false;
    while (robot->step(TIME_STEP) != -1) {
        bool leftSensor = (dsl->getValue() < 950.0);
        bool rightSensor = (dsr->getValue() < 950.0);

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
        else */if (leftSensor) {
            //Left
            leftMotor->setVelocity(-MAX_SPEED);
            rightMotor->setVelocity(MAX_SPEED);
        }
        else if (rightSensor) {
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