## <h1 align="center">ARTICULATED MANIPULATOR
 
## <h2 align="center"> Abstract 
<img align="left" alt = "Coding" width="135" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/1f51c48d-83c9-41cc-a03b-464adfa76a4d">
<h5 align="justify">  This repository will serve as Group 13-Articulated, Midterm project in Robotics 2. This focuses on the Articulated Manipulator, providing an overview of the important characteristics such as calculating the degrees of freedom (DOF) and employing Denavit-Hartenberg (D-H) Notation for the joint parameters. Furthermore, forward and reverse kinematics for joint angles and the position of the end-effector will also be tackled. To further clarify the concepts of how an Articulated Manipulator functions, more images, and descriptions are also included. 

## <h2 align="center">TABLE OF CONTENTS:
<h4 align="center">  
 
  [I. Introduction](#i-introduction)
  
  [II. Degrees of Freedom](#ii-degrees-of-freedom)
  
  [III. Kinematic Diagram and D-H Frame](#iii-kinematic-diagram-and-d-h-frame)
  
  [IV. D-H Parametric Table](iv-d-h-parametric-table)
  
  [V. Homogeneous Transformation Matrix](v-homogeneous-transformation-matrix)
  
  [VI. Inverse Kinematics](v-homogeneous-transformation-matrix)
  
  [VII. Forward and Inverse Kinematics GUI Calculator](vii-forward-and-inverse-kinematics-gui-calculator)
  
  [VIII. References](viii-references)
  
  [IX. Curriculum Vitae](#our-team)

## <h2 align="center">I. INTRODUCTION
<img align="right" alt = "Python" width="300" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/befaf219-f7f4-46e6-8c83-3bb39b83a67e">

 <h5 align="justify"> Articulated Manipulators also called Robotic Arms are known for their high adaptability and versatility to perform widespread functions. In 1950, Articulated Manipulators were introduced for manufacturing processes. Afterward, They substantially developed and now play a crucial role in a variety of fields, including the automobile, aerospace, healthcare, and research. The value of articulated robots is derived from their capacity to increase efficiency, precision, and safety in a variety of processes. These robots are meant to conduct repetitive and risky jobs that people typically find too difficult or unsafe to execute. 
</p>
   As the years passed, Articulated Manipulators undertook an innovation to take full advantage and unlock the full potential of their automation processes and make them more efficient. As a result, due to its ability to move quickly and precisely, it is used in manufacturing from assembly to material handling. In addition, Articulated Manipulators are now often used in Healthcare, Agriculture, Military Defense, and Education. With the help of advanced sensors, artificial intelligence, and adaptive algorithms, Articulated Manipulators continually improve their capabilities. For a variety of reasons, articulated robots are ideal for assembly applications. Their joints enable them to move in ways that other robots do not. Their payload capacity also allows them to transport items that other robot kinds cannot. They are accurate enough for even minor assembly operations. 

## <h2 align="center">II. DEGREES OF FREEDOM
  <h5 align="justify"> In robotic arms, a 'Degree of Freedom' (DoF) is an independent joint that allows the manipulator to move in either a rotational or translational (linear) direction. In addition, a robot's ability to move along how many independent axes or motions. It stands for the total number of independent parameters that affect how the robot is configured or posed. 
</p>
Accordingly, to solve a DOF of a specific manipulator the first thing to do is to determine whether it is a spatial with 6 DOF or planar with 3 DOF. The next step is to figure out the number of joints and moving links on the manipulator. After that, the calculation of the number of joint constraints in the given manipulator and determining if it is spatial or planar with the help of Grubler’s Criterion. Lastly is to determine the types of manipulator based on the number of degrees of freedom. 
</p>	  
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/5db25ea5-3888-4eb5-8b61-a97bce2d930e">
</p>
<h4 align="justify">Types of Manipulator based on the Number of Degrees of Freedom
<h5 align="left">
 
 __Under-actuated Manipulator__
+ Either a Spatial Manipulator w/less than 6-DOF or a Planar Manipulator w/less than 3-DOF. 

__Ideal Manipulator__ 
+ Either a Spatial Manipulator w exactly 6-DOF or a Planar Manipulator w/exactly 3-DOF. 

__Redundant Manipulator__ 
+ Either a Spatial Manipulator w/more than 6-DOF or a Planar Manipulator w/more than 3-DOF. 

<h5 align="justify"> Calculating the DOF of an articulated manipulator allows you to grasp its capabilities and limitations, enabling you to design, program, and control these remarkable machines effectively. An articulated manipulator, often referred to as a robotic arm, consists of interconnected links and joints that mimic the movement capabilities of a human arm. Each joint provides a rotational or translational degree of freedom, allowing the manipulator to perform intricate tasks with remarkable dexterity. By calculating the DOF, we can quantitatively determine the range of motions and positions that the manipulator can achieve. The Articulated Manipulator has a total of 3 degrees of freedom that consist of 3 revolute joints also referred to as RRR (REVOLUTE REVOLUTE REVOLUTE).
   <p align="center">
  <mp4 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/d74e24ea-5b11-4efb-b1b7-a66115e37dfd">
</p>
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/32493d2c-c98d-404a-96bb-39aace8f6107">
</p>
<h4 align="center">Supplementary Video about the Degrees of Freedom
<h5 align="center">To further understand how to get the Degrees of Freedom of an Articulated Manipulator, here is a supplementary video explaining how to get it.  
</p> 
 <a href="https://drive.google.com/file/d/13NccGlxma1fw7g3MDnbqmGmPHvtEQ4wS/view">
    <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/69f0608b-6055-49a4-9c53-84936f0e0aff>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/69f0608b-6055-49a4-9c53-84936f0e0aff" alt="Discussion of Degrees of Freedom for the Articulated Manipulator" width = 600 title="Discussion of Degrees of Freedom for the Articulated Manipulator">
</a>    

 ## <h2 align="center">III. Kinematic Diagram and D-H Frame
<h5 align="justify">The Denavit-Hartenberg Notation, often known as D-H Notation, was developed in 1995 by Jacques Denavit and Richard Hartenberg to standardize coordinate frames for spatial links.   
</p>	
To solve the forward kinematics of a mechanical manipulator we will use the DH Notation (Denavit-Hartenberg Notation). 
</p> 
 
 + The D-H notation offers a systematic approach to express the geometric configuration of robotic systems, making kinematic analysis and modeling easier.
 + It is frequently used in robotics, particularly industrial robot systems and robot arms with manipulators.

In DH notation, there are some preliminary rules and main rules that define how to assign coordinate frames and determine the parameters for each joint. 
</p> 
<h4 align="justify">D-H Frame Preliminary Rules
<h5 align="justify">

+ Rule 1:  Decide first the 3 views you want to project on your isometric drawing
</p> 

+ Rule 2: Identify the center of your frames
</p> 

+ Rule 3: Then draw your color coded arrows based on your decided 3 views.
  + Blue - z axis
  + Red - x axis
  + Green - y axis
<p align="left" width="200">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/efc4d132-c897-46c8-876a-2a110b61faee">
</p> 

+ Rule 4: Remember to make the arrows of Z and X axes easy to see for the future computations
  + Y axis less important than X and Z axes

</p> 
<h4 align="justify">D-H Frame Rules
</p> 
<h5 align="justify"> NOTE: THE COUNTING OF FRAMES STARTS FROM 0 (FROM THE FORMULA N-1)
<h5 align="justify">
<img align="right" alt="Coding" width="220" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/c508c14f-61ca-4ead-a578-ded4920210a6">

+ Rule 1: The Z axis must be the axis of rotation for a revolute/twisting, or the direction of translation for a prismatic joint. (Labels starts from Z0)
</p> 

+ Rule 2: The X axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it. (Labels starts from X0)
</p> 

+ Rule 3: Each X axis must intersect the Z axis of the frame before it. Rules for complying Rule 3:
  + Rotate the axis until it hits the other.
  + Or translate the axis until it hits the other.

</p> 

+ Rule 4: All frames must follow the right-hand rule (Labels starts from Y0)
</p> 
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/48aa53c2-d20d-4cd8-95fb-3c8715806f14">
</p>
<h4 align="center">Supplementary Video about the Kinematic Diagram and D-H Frame
<h5 align="center">To further understand how to get the Kinematic Diagram and D-H Frame, here is a supplementary video explaining how to get it.  
 <a href="https://drive.google.com/file/d/1CX_0pApp5kKIIYxm54IEQ58krmHvNwGa/view">
 <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/4d78e754-6d0c-4092-9aa8-40d49bbee576>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/0836528d-49da-4a64-ab87-37b3838f418e" alt="Discussion of Kinematic Diagram and D-H Frame for the Articulated Manipulator" width = 600 title="Discussion of Kinematic Diagram and D-H Frame for the Articulated Manipulator">
</a>   
 
## <h2 align="center">IV. D-H PARAMETRIC TABLE
<h5 align="justify">The Denavit-Hartenberg parameters (also called D-H parameters) are the four parameters associated witha particular convention for attaching reference frames to the links of a spatial kinematic chain,or robot manipulator.
</p>
The Denavit-Hartenberg parameter tables consist of four variables:
</p>
 
 + θ (theta) - rotation around zₙ₋₁ that is required toget xₙ₋₁ to match xₙ, with the joint variable θ if joint is revolute/twisting joint.
</p>

+ a (alpha) - rotation around xₙ that is required to match zₙ₋₁ to zₙ.
</p>

+ d - The distance from the origin of n-1 and n frames along the zₙ₋₁ direction, with joint variable if joint is prismatic.
</p>

+ r - The distance from the origin of n-1 and n frames along the xₙ₋₁ direction.

<h5 align="justify">The Articulated Manipulator consists of three revolute joints and it can be seen on the three frames of the manipulator from frame 0, frame 1, and frame 2.   
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/eb629da0-c230-4238-a76b-7d147f5b7033">
</p>
<h5 align="justify">As seen in the table is parametric table of articulated manipulator, each column represents the number of parameters that are needed to complete the table such as parameter theta and alpha which represents the rotation of the manipulator, and the parameter r and d which represents the translation of the manipulator per frame.   
</p> 
<h4 align="center">Supplementary Video about the D-H Parametric Table of Articulated Manipulator 
<h5 align="center">To further understand how to get the D-H Parametric Table, here is a supplementary video explaining how to get it.  
 <a href="https://drive.google.com/file/d/18cw6NJNt64Ajvra6pkWnRcIHqiqVB5f5/view?usp=sharing">
 <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/7ffbb227-fb39-4027-818f-427895ec2b5f>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/7ffbb227-fb39-4027-818f-427895ec2b5f" alt="Discussion of D-H Parametric Table for the Articulated Manipulator" width = 600 title="Discussion of D-H Parametric Table for the Articulated Manipulator">
</a>   
 
 ## <h2 align="center">V. HOMOGENEOUS TRANSFORMATION MATRIX
<h5 align="justify">Homogeneous transformation matrices combine both the rotation matrix and the displacement vector into a single matrix. Homogeneous transformation matrices combine both the rotation matrix and the displacement vector into a single matrix. You can multiply two homogeneous matrices together just like you can with rotation matrices. Homogeneous transformation matrices enable us to combine rotation matrices (which have 3 rows and 3 columns) and displacement vectors (which have 3 rows and 1 column) into a single matrix. They are an important concept of forward kinematics.  
</p> 
 
![image](https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/a6c1a861-a229-469e-8409-2d841ef4ce90)
<h5 align="justify">Homogeneous transformation matrix, denoted as H and it also has a superscript for reference frame and subscript for the projected frame. The matrix shown is the formula in obtaining the homogeneous transformation matrix, it has a 4x4 matrix that composed of 3x3 Rotation matrix combined with 3x1 position vector and 1x4 augmentation column composed of 0 0 0 1.
<h5 align="justify">The following figures are the calculation of homogeneous transformation matrix of articulated manipulator.
</p> 

 ![image](https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/3fc9e382-f819-48d9-a585-a8c6a9bfb65e)
![image](https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/013fb789-dc98-4894-be19-e48ea0ae469b)
![image](https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/d6c95b63-786e-4e96-a039-384e433483e8)
<h4 align="center">Supplementary Video about the Homogeneous Transformation Matrix of Articulated Manipulator 
<h5 align="center">To further understand how to get the Homogeneous Transformation Matrix, here is a supplementary video explaining how to get it.
 <a href="https://drive.google.com/file/d/1CfDKDjL68Fsk21M647CW5w04_R1Caz6K/view?usp=sharing">
 <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/2165f469-39ff-4402-b4fb-1f34ad4956c4>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/2165f469-39ff-4402-b4fb-1f34ad4956c4" alt="Discussion of Homogeneous Transformation Matrix for the Articulated Manipulator" width = 600 title="Discussion of Homogeneous Transformation Matrix for the Articulated Manipulator">
</a>   

## <h2 align="center">VI. INVERSE KINEMATICS USING GRAPHICAL METHOD
<h5 align="justify">Inverse Kinematics  is the technique of computing joint angles using the end-effector's location and orientation.  In addition, Inverse kinematics simply requires a static set of joint angles to position a certain point (or combination of points) of the character (or robot) at a specific location. 
 </p> 
 In comparison, Forward kinematics computes the chain's configuration using the joint parameters, whereas inverse kinematics reverses this computation to determine the joint parameters that produce the desired configuration. In contrast to the concept of forward kinematics, which involves determining the workspace coordinates of a robot based on a given configuration, inverse kinematics (IK) represents the inverse process. It entails calculating the appropriate configuration(s) to achieve a desired workspace coordinate. This operation holds significant value in various robotics applications, including the movement of tools along specified paths, object manipulation, and capturing scenes from desired viewpoints. 
</p>  
 In forward kinematics the given inputs are the joint variables, using the homogeneous transformation matrix, we will obtain the output, position vector. 
<p align="center">
  <img width="700"  src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/0f5f58d9-674d-49a3-a218-ee3ef85a12ad">
</p>  
While in inverse kinematics, the given input is the position vector, while the output is the joint variable, the method to obtain the output is depends on the design of difficulty of the mechanical manipulator.   
<p align="center">
  <img width="700" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/84874595-5171-4371-879b-98f0b53db9dd">
</p> 
The inverse kinematics function or algorithm takes a target position as its input and computes the necessary pose for the end effector to attain the target position, producing the pose as the output. In the realm of robotics, it can determine the optimal movements of a robotic arm to ensure that an actuator located at the arm's end is accurately positioned. Similarly, within the context of three-dimensional animation, inverse kinematics can be employed in animation software, allowing the movement of a subordinate joint in a hierarchical character rig to naturally influence parent objects. Due to its paramount importance, extensive research has been conducted on inverse kinematics, resulting in numerous techniques that facilitate efficient and reasonably reliable solutions. 

<h4 align="center">INVERSE KINEMATICS CALCULATION OF ARTICULATED MANIPULATOR (RRR)
<h5 align="center">Inverse Kinematic Diagram (Top View)
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/2d03d5e0-33f1-43df-8eb7-3442e880f1aa">
  </p>
  <h4 align="center">Inverse Kinematic Diagram (Front View)
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/3ca715be-2439-4d75-9d33-6348f2ede67c">
  </p>
<h4 align="center">Supplementary Video about the Inverse Kinematics of Articulated Manipulator 
<h5 align="center">To further understand how to get the Inverse Kinematics, here is a supplementary video explaining how to get it.  
 <a href="https://drive.google.com/file/d/1-gFm7NqfxsCYq6r9rKb2YGz5jvkMfqIG/view?usp=sharing">
 <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/b84d8bfe-8a95-426a-b81a-ef5a5e81ef67>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/a88c68d3-21d7-4813-9923-17ce34bfaf3d" alt="Discussion of Inverse Kinematics for the Articulated Manipulator" width = 600 title="Discussion of Inverse Kinematics for the Articulated Manipulator">
</a>   
 
## <h2 align="center">VII. FORWARD AND INVERSE KINEMATICS GUI CALCULATOR
<h5 align="justify">GUI calculator is only a calculator but one can use it by clicking buttons, not by typing something like in python print(2+2), and then will get the result as 4 in the black and white environment. In the GUI calculator, all its operators and numbers are represented graphically and one can click it and use it. GUI is simply a visual and more easy-to-use way to interact with a computer, example: one will easily click a button to know what time it is. But it will be more complex to type “time” to get the current time.
<h5 align="justify">Below figure is the calculator created using python, it is used to compute an articulated manipulator's forward and inverse kinematics.
 <p align="center">
  <img width=300 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/f5f8d1a0-081e-454f-a9d2-30af4392627e">
<h4 align="center">Simulation of Calculators
</p> 
 <a href="https://drive.google.com/file/d/1XRXWK5P27zj8uTAFQfOhpmAZgihVD4It/view?usp=sharing">
 <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/6cc8bea9-88d4-4b98-a38c-3335be7b9f08>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/6cc8bea9-88d4-4b98-a38c-3335be7b9f08" alt="Discussion of Inverse Kinematics for the Articulated Manipulator" width = 600 title="Discussion of Inverse Kinematics for the Articulated Manipulator">
</a>   

## <h2 align="center">VIII. REFERENCES
<h5 align="left">
 
 + Articulated Robots: A guide to the most familiar industrial robot. (n.d.). HowToRobot. https://howtorobot.com/expert-insight/articulated-robots
 + Automaticaddison, A. (2020, August 26). Find homogeneous transformation matrices for a robotic arm – automatic addison. https://automaticaddison.com/find-homogeneous-transformation-matrices-for-a-robotic-arm/#:~:text=Homogeneous%20transformation%20matrices%20combine%20both,frame%200%20to%20frame%202
 + Denavit-Hartenberg notation. (n.d.). Robot Academy. https://robotacademy.net.au/lesson/denavit-hartenberg-notation/#:~:text=In%20the%20Denavit%2DHartenberg%20notation,translation%20along%20the%20Z%20axis
 + Ganti, A. (2024, February 28). Degrees of freedom in statistics explained: Formula and example. Investopedia. https://www.investopedia.com/terms/d/degrees-of-freedom.asp#:~:text=Degrees%20of%20freedom%20refer%20to,items%20within%20the%20data%20sample
 + Government of Canada, Canadian Centre for Occupational Health and Safety. (2024, February 10). Hazard and risk - Hazard identification. https://www.ccohs.ca/oshanswers/hsprograms/hazard/hazard_identification.html
 + Kala, R. (2024). An introduction to robotics. In Elsevier eBooks (pp. 1–48). https://doi.org/10.1016/b978-0-443-18908-1.00010-8
 + Khatri, A. (2022, March 15). GUI calculator using tkinter Python. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2022/01/gui-calculator-using-tkinter-python/#:~:text=GUI%20calculator%20is%20only%20a,click%20it%20and%20use%20it
 + Rao, R. (2023, March 26). What are Articulated Robots? Anatomy, Control Systems, Advantages, Selection Criteria, and Applications. Wevolver. https://www.wevolver.com/article/what-are-articulated-robots-anatomy-control-systems-advantages-selection-criteria-and-applications
 + Robotics, R. (2021, December 10). ‘DEGREES OF FREEDOM’ VS ‘FUNCTIONS’ OF a ROBOTIC ARM. REACH ROBOTICS. https://reachrobotics.com/blog/degrees-of-freedom-vs-functions-of-a-robotic-arm/
 + Understanding robot coordinate frames and points. (n.d.). https://www.solisplc.com/tutorials/robot-coordinate-frames-and-points
 + Wikipedia contributors. (2023, November 26). Inverse kinematics. Wikipedia. https://en.wikipedia.org/wiki/Inverse_kinematics
 + Wikiwand - Carl Jacobi. (n.d.). Wikiwand. https://www.wikiwand.com/it/Carl_Jacobi

## <h2 align="center">Our Team 

<h4 align="center">
<p align="center">
  <img width=100 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/e2d2e5c6-c1e2-4dfe-b04f-a59df4c76d1b">  
 
[Abong, Louwella](#abong-louwella-p) (PL - Project Leader)

<p align="center">
  <img width=100 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/eb02b986-ff9c-4050-82c8-802cbf615d4c">  
 
[Atienza, Ma. Angela](#atienza-ma-angela-e) (PQ - Project Quality Engineer)
<p align="center">
  <img width=100 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/3829d65b-1883-4b0e-9117-1e984b7c5225"> 
 
[Marasigan, Stanlee](#marasigan-stanlee-b) (PP - Project Programmer)
<p align="center">
  <img width=100 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/f164b48a-d05e-47b4-9f5d-b802e1fecf1c">    
 
[Reyes, Shervin](#reyes-shervin-d) (PS - Project Supervisor)
</p> 

Instructor: Engr. Mikko De Torres 
<p align="center">
  <img width=100 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/da136adb-5377-49fc-999d-c3dcd3659541">
  </p> Mechatronics Engineer
</p> Robotics 2, Instructor



<h2 align="center">Curriculum Vitae

## Abong, Louwella P.
<p align="center">
  <img width=400 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/66718567-828b-4e3a-a80d-460eb2a9651f">  
 
## Atienza, Ma. Angela E. 
<p align="center">
  <img width=400 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/e7d22d5e-bd47-47b5-9b3f-95e8f99965a9">

## Marasigan, Stanlee B.
<p align="center">
  <img width=400 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/e8a61f91-9970-4084-9ce0-02a260a3401a">
 
## Reyes, Shervin D.
<p align="center">
  <img width=400 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/34f99327-fe7b-4c9e-8082-cec44a0dead9">
  
