#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/Camera.hpp>
#include <webots/TouchSensor.hpp>

#define TIME_STEP 64
#define MAX_SPEED .5
#define MAX_CAMERA_SPEED 2.0

// All the webots classes are defined in the "webots" namespace
using namespace webots;

// All components of the robot
static Motor* leftMotor;
static Motor* rightMotor;
static TouchSensor* leftSensor;
static TouchSensor* rightSensor;
static Camera* camera;
static Motor* cameraMotor;

// High level functions
static void MoveForward() {
    leftMotor->setVelocity(MAX_SPEED);
    rightMotor->setVelocity(MAX_SPEED);
}

static void MoveBack() {
    leftMotor->setVelocity(-MAX_SPEED);
    rightMotor->setVelocity(-MAX_SPEED);
}

static void TurnLeft() {
    leftMotor->setVelocity(-MAX_SPEED);
    rightMotor->setVelocity(MAX_SPEED);
}

static void TurnRight() {
    leftMotor->setVelocity(MAX_SPEED);
    rightMotor->setVelocity(-MAX_SPEED);
}

static void DriveForward(double angle, bool inRadians = false) {
    if (inRadians) {
        angle *= 57.295;//180/3.14 = 57
    }
    if (angle > 90 || angle < -90) {
        return;
    }
    else if (angle >= 0) {
        leftMotor->setVelocity(MAX_SPEED);
        rightMotor->setVelocity(MAX_SPEED * sin((angle + 45) / 28.648) );
    }
    else {
        leftMotor->setVelocity(MAX_SPEED * sin((-angle + 45) / 28.648) );
        rightMotor->setVelocity(MAX_SPEED);
    }
}

static void TurnCameraUp() {
    cameraMotor->setVelocity(-MAX_CAMERA_SPEED);
}

static void TurnCameraDown() {
    cameraMotor->setVelocity(MAX_CAMERA_SPEED);
}

static void ResetMotors() {
    leftMotor->setVelocity(0);
    rightMotor->setVelocity(0);
    cameraMotor->setVelocity(0);
}

int main(int argc, char** argv) {
    //Create the robot instance.
    Robot* robot = new Robot();

    //Set up motor/track wheels
    leftMotor = robot->getMotor("leftMotor");
    rightMotor = robot->getMotor("rightMotor");
    leftMotor->setPosition(INFINITY);
    rightMotor->setPosition(INFINITY);

    //Set up touch sensors
    leftSensor = robot->getTouchSensor("left sensor");
    rightSensor = robot->getTouchSensor("right sensor");
    leftSensor->enable(TIME_STEP);
    rightSensor->enable(TIME_STEP);

    //Set up camera and camera motor
    camera = robot->getCamera("camera");
    camera->enable(TIME_STEP);
    cameraMotor = robot->getMotor("camera motor");
    cameraMotor->setPosition(INFINITY);
    cameraMotor->setVelocity(0.0);

    //Local variables
    //int examlpeNum = 0;

    //Robot AI goes here
    for (int i = 0; i < 3; i++) {
        MoveForward();
        robot->step(TIME_STEP * 18);
        ResetMotors();
        robot->step(TIME_STEP);
        TurnRight();
        robot->step(TIME_STEP * 18);
        ResetMotors();
        robot->step(TIME_STEP);
    }

    MoveForward();
    robot->step(TIME_STEP * 18);
    ResetMotors();
    robot->step(TIME_STEP);
    TurnLeft();
    robot->step(TIME_STEP * 17);

    for (int i = 0; i < 4; i++) {
        TurnLeft();
        robot->step(TIME_STEP * 18);
        ResetMotors();
        robot->step(TIME_STEP);
        MoveBack();
        robot->step(TIME_STEP * 18);
        ResetMotors();
        robot->step(TIME_STEP);
    }
    
    TurnLeft();
    robot->step(TIME_STEP * 35);
    ResetMotors();
    robot->step(TIME_STEP);

    /*while (robot->step(TIME_STEP) != -1) {
        //Print any test messages here
        //std::cout << "Hello, World!" << std::endl;

        //Touch sensors are doubles of either 1 or 0
        bool leftSensorActivated = leftSensor->getValue();
        bool rightSensorActivated = leftSensor->getValue();

        DriveForward(-75.0);
    }*/

    //End of AI
    ResetMotors();
    delete robot;
    return 0;  // EXIT_SUCCESS
}