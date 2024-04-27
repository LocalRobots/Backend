<!-- Webots Challenges -->

## Purpose
<!-- About The Project -->  
This is a Bradley University CS capstone project, currently designing and developing robot prototypes and testing thereof for usage in a related Bradley AI course. Feedback to this repository in labeling points of improvement will help to benefit current and future students usage of this project's and it's outcomes.

!!!This Project Documentation is currently in development and subject to change!!!

<!-- future screenshots -->

---

<details>
 <summary>Webots Setup</summary>
  <ol>
  <!--Webots Setup -->

  Webot's site can be found at [https://cyberbotics.com/](https://cyberbotics.com/) where you will find the installer download on the homepage.

  Confirm the correct operating system installer as shown below the download button, using the arrow dropdown menu next to the download button if it does not match your system.

  * Run the installer you just downloaded
  * On Windows, in the case of an 'Windows protected your PC' warning prompt, click on 'More info' and then confirm to run
  * Follow the install wizard dialogues and installations to finish setting up Webots!

  <!--Understanding Webots -->

  Let's start by opening up the Webots tutorial world: 
  * In the file explorer open up the 'world' file from this repository located at "...AI-Robots-Challenges\Webots\worlds\moose_demo.wbt"
  * When you open up Webots for the first time, you'll be prompted to choose a theme, continue by selecting 'Start Webots with the selected theme'
  * Congrats, you've successfully loaded the world! Here you can get accustomed to the environment and interface
    
  This 'world' you opened up is one of Webot's open source demo worlds. Here, the robot demonstates simple movement ai that traverses between defined checkpoints. 

  Take note of some important features of the interface:
  * To rotate the camera, hold left-click while moving your mouse inside the simulation window
  * To move the camera, hold right-click while moving your mouse inside the simulation window
  * The left side of the interface contains the hierarchy of nodes (similar to objects)
  * The right side contains the built in text editor section where you can edit scripts inside the program
  * Above the simulation window, you'll find the main functions for the simulation, tooltip information is displayed when hovered over the different functions
  * The 'pause/play' function starts or pauses the current world simulation
  * To the left of that, the '|<<' function resets the time of the simulation to 0
  * Pausing the simulation before resetting will keep the simulation in a paused state after resetting
  
  <!--GitHub Setup-->
  ---

  If you are a student or someone that would like to go through the challenges yourself, creating your own clone of the repository can be accomplished as follows:
  * Download and install 'Github Desktop' from [https://desktop.github.com/](https://desktop.github.com/)
  * Go to 'File' -> 'Clone a repository', and the after selecting the URL tab input the URL of this repository, otherwise on the Github webpage of the repository, click the '<> Code' dropdown and select 'Open with Github Desktop'
  * Once cloned, you now have your own version of the project and upload your personal projects to your own Github
  
  Now that you have the project files, you may explore the various challenges and worlds provided. The first challenge is located at "...AI-Robots-Challenges\Webots\worlds\FirstChallenge.wbt".

  ---
  
  Provided below are the student challenges, designed to help student's understanding of various AI principle and test code for their robots functionality before transferring to the physical hardware.

 </ol>
</details>




<details>
  <summary>Message For Future Capstone</summary>
  <ol>
 
 ## This GitHub

 This Github contains various prototypes and testing worlds for Webots. This includes Proto files, which can be added into Webots worlds. Additionally there is code for the physical robot seporately. We do have a google drive [https://drive.google.com/drive/folders/1pGyogeERTkXf6sNzcHc3qFW8bzAnDlqE?usp=sharing](https://drive.google.com/drive/folders/1pGyogeERTkXf6sNzcHc3qFW8bzAnDlqE?usp=sharing) that contains a few useful files. This repo should contain files that students don't need or personal tests. The Challenges repo should contain only the nessisary materials for students.

 ## Future Considerations

 The new capstone team is allowed to disregard these suggestions for improvement, but we think that the following could be improved
 * Backend repo
   * Organized & remove redundent files/worlds (keep atleast 1 robot with tracks because tracks are hard to set up)
   * A proper ReadMe
   * Include solutions for each challenge
 * Student challenges repo
   * Explaining timestep better
   * Include a feedback/bug report form
   * Improved collision detection (it is likely impossible to fix, posibly change world timestep)
   * Error messages from objects with the same name
 * Physical robot
   * Documentation
 
 ---
 
</ol>
</details>






<!--## Project Setup

If you had forked this repository, sync the respotory

* In the top right corner of the GitHub page that was forked, under the green code button hit the sync fork button
* Click Update branch (you may need to refresh the page to see changes)
* Fetch changes from GitHub desktop

Let's open up the Webots world

* In the file explorer open up the file from this GitHub at ...AI-Robots-Challenges\Webots\worlds\SecondChallenge.wbt
-->

<!--## Coding with the camera

Since last challenge, there are more functions, that aren't necessary for this challenge, but could be helpful. DriveForward(angle) and TurnCameraUp()/TurnCameraDown(). The TurnCamera functions are work in progress because the camera can turn inside the robot.

The AI starts on line 101, and I've premade a while loop that prints the RGB of a pixel on the camera. Specifically the bottom middle pixel. This is done by imageGetColor(Image, width, x, y) function. You can see the camera in the top left corner of the simulation window. If you move the middle ball and use the red arrow to drag it toward the robot, the print statement will change.
-->

<!--<img src="Images/Challenge2.png" width = "500" >

* Now try the parallel parking challenge
* Once you complete it, feel free to move Evil Duck onto the top of the track for extra credit.

-->
## Repository Feedback

If you haven't already completed the google form, please feel free to add your input to our project here as it is much appreciated: [Feedback Form](https://forms.gle/rBniEH7UuqJXANCg7) 
