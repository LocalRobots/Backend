//#include <webots/DistanceSensor.hpp>
#include <webots/Motor.hpp>
#include <webots/Robot.hpp>

#include <webots/keyboard.hpp>

#define TIME_STEP 64
#define MAX_SPEED 5.0
using namespace webots;

int main(int argc, char** argv) {

    Robot* robot = new Robot();
    /*DistanceSensor *ds[2];
    char dsNames[2][10] = {"ds_right", "ds_left"};
    for (int i = 0; i < 2; i++) {
      ds[i] = robot->getDistanceSensor(dsNames[i]);
      ds[i]->enable(TIME_STEP);
    }*/
    Motor* wheels[2];
    char wheels_names[2][8] = { "Wheel1", "Wheel2" };
    for (int i = 0; i < 2; i++) {
        wheels[i] = robot->getMotor(wheels_names[i]);
        wheels[i]->setPosition(INFINITY);
        wheels[i]->setVelocity(0.0);
    }
    //int avoidObstacleCounter = 0;
    Keyboard keyboard = Keyboard();
    keyboard.enable(TIME_STEP);

    while (robot->step(TIME_STEP) != -1) {
        double leftSpeed = 0.0;
        double rightSpeed = 0.0;
        /*if (avoidObstacleCounter > 0) {
          avoidObstacleCounter--;
          leftSpeed = 1.0;
          rightSpeed = -1.0;
        } else { // read sensors
          for (int i = 0; i < 2; i++) {
            if (ds[i]->getValue() < 950.0)
              avoidObstacleCounter = 100;
          }
        }*/

        int key = keyboard.getKey();
        if (key >= 0) {
            if (key == keyboard.UP) {
                leftSpeed = MAX_SPEED;
                rightSpeed = MAX_SPEED;
            }
            else if (key == keyboard.DOWN) {
                leftSpeed = -MAX_SPEED;
                rightSpeed = -MAX_SPEED;
            }
            else if (key == keyboard.RIGHT) {
                leftSpeed = MAX_SPEED;
                rightSpeed = -MAX_SPEED;
            }

            else if (key == keyboard.LEFT) {
                leftSpeed = -MAX_SPEED;
                rightSpeed = MAX_SPEED;
            }
        }

        wheels[0]->setVelocity(leftSpeed);
        wheels[1]->setVelocity(rightSpeed);
    }
    delete robot;
    return 0;  // EXIT_SUCCESS
}