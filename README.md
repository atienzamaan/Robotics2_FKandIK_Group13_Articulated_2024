<h1 align="center">ARTICULATED MANIPULATOR

## <h2 align="center"> Abstract 
<h4 align="justify">  This repository will serve as Group 13-Articulated, Midterm project in Robotics 2. This focuses on the Articulated Manipulator, providing an overview of the important characteristics such as calculating the degrees of freedom (DOF) and employing Denavit-Hartenberg (D-H) Notation for the joint parameters. Furthermore, forward and reverse kinematics for joint angles and the position of the end-effector will also be tackled. To further clarify the concepts of how an Articulated Manipulator functions, more images, and descriptions are also included. 

## <h2 align="center">TABLE OF CONTENTS:
<h3 align="center">  
 
  [I. Introduction](#i-introduction)
  
  [II. Degrees of Freedom](#ii-degrees-of-freedom)
  
  [III. Kinematic Diagram and D-H Frame](#iii-kinematic-diagram-and-d-h-frame)
  
  [IV. D-H Parametric Table](iv-d-h-parametric-table)
  
  [V. Homogeneous Transformation Matrix](v-homogeneous-transformation-matrix)
  
  [VI. Inverse Kinematics](v-homogeneous-transformation-matrix)
  
  [VII. Forward and Inverse Kinematics GUI Calculator](vii-forward-and-inverse-kinematics-gui-calculator)
  
  [VIII. References](viii-references)
  
  [IX. Our Team](#our-team)

## <h2 align="center">I. INTRODUCTION
 <img align="left" alt="Coding" width="400" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/1f51c48d-83c9-41cc-a03b-464adfa76a4d">

  <h4 align="justify"> </div> Articulated Manipulators also called Robotic Arms are known for their high adaptability and versatility to perform widespread functions. In 1950, Articulated Manipulators were introduced for manufacturing processes. Afterward, They substantially developed and now play a crucial role in a variety of fields, including the automobile, aerospace, healthcare, and research. The value of articulated robots is derived from their capacity to increase efficiency, precision, and safety in a variety of processes. These robots are meant to conduct repetitive and risky jobs that people typically find too difficult or unsafe to execute. 
</p> 
</p>
   As the years passed, Articulated Manipulators undertake an innovation to take full advantage and unlock the full potential of their automation processes and make them more efficient. As a result, due to its ability to move quickly and precisely, it is used in manufacturing from assembly to material handling. In addition, Articulated Manipulators are now often used in Healthcare, Agriculture, Military Defense, and Education. With the help of advanced sensors, artificial intelligence, and adaptive algorithms, Articulated Manipulators continually improve their capabilities. For a variety of reasons, articulated robots are ideal for assembly applications. Their joints enable them to move in ways that other robots do not. Their payload capacity also allows them to transport items that other robot kinds cannot. They are accurate enough for even minor assembly operations. 
   
## <h2 align="center">II. DEGREES OF FREEDOM

  <h4 align="justify"> In robotic arms, a 'Degree of Freedom' (DoF) is an independent joint that allows the manipulator to move in either a rotational or translational (linear) direction. In addition, a robot's ability to move along how many independent axes or motions. It stands for the total number of independent parameters that affect how the robot is configured or posed. 
</p>
Accordingly, to solve a DOF of a specific manipulator the first thing to do is to determine whether it is a spatial with 6 DOF or planar with 3 DOF. The next step is to figure out the number of joints and moving links on the manipulator. After that, the calculation of the number of joint constraints in the given manipulator and determining if it a spatial or planar with the help of Grubler’s Criterion. The Articulated Manipulator has a total of 3 degrees of freedom that consist of 3 revolute joints also referred to as RRR (REVOLUTE REVOLUTE REVOLUTE).  
</p>	  
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/5db25ea5-3888-4eb5-8b61-a97bce2d930e">
</p>
<p align="center">
  <mp4 src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/d74e24ea-5b11-4efb-b1b7-a66115e37dfd">
</p>
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/32493d2c-c98d-404a-96bb-39aace8f6107">
</p>
<h3 align="center">Supplementary Video about the Degrees of Freedom
<h4 align="center">To further understand how to get the Degrees of Freedom of an Articulated Manipulator, here is a supplementary video explaining how to get it.  
</p>
<p href="https://drive.google.com/file/d/13NccGlxma1fw7g3MDnbqmGmPHvtEQ4wS/view">
    <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/69f0608b-6055-49a4-9c53-84936f0e0aff>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/69f0608b-6055-49a4-9c53-84936f0e0aff" alt="Discussion of Degrees of Freedom for the Articulated Manipulator" width = 600 title="Discussion of Degrees of Freedom for the Articulated Manipulator">
    
## <h2 align="center">III. Kinematic Diagram and D-H Frame
<img align="right" alt="Coding" width="250" src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/fbc7cfb9-1cdc-4493-994e-eaa1986e882c">
 <h4 align="justify"> The Denavit-Hartenberg Notation, often known as D-H Notation, was developed in 1995 by Jacques Denavit and Richard Hartenberg to standardize coordinate frames for spatial links.   
</p>	
To solve the forward kinematics of a mechanical manipulator we will use the DH Notation (Denavit-Hartenberg Notation). The D-H notation offers a systematic approach to express the geometric configuration of robotic systems, making kinematic analysis and modeling easier. It is frequently used in robotics, particularly industrial robot systems and robot arms with manipulators. In DH notation, there are some preliminary rules and main rules that define how to assign coordinate frames and determine the parameters for each joint. When implementing D-H Notation, these rules are utilized to allocate frames in a kinematic diagram. One of the rules is that we must utilize the "Right Hand Rule" to decide where to locate the X, Y, and Z axes.  
</p>
<p align="center">
  <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/48aa53c2-d20d-4cd8-95fb-3c8715806f14">
</p>
<h3 align="center">Supplementary Video about the Kinematic Diagram and D-H Frame
<h4 align="center">To further understand how to get the Kinematic Diagram and D-H Frame, here is a supplementary video explaining how to get it.  
</p>
<a href="https://drive.google.com/file/d/1CX_0pApp5kKIIYxm54IEQ58krmHvNwGa/view">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/4d78e754-6d0c-4092-9aa8-40d49bbee576>
    <img src="https://github.com/stnll/Robotics2_FKandIK_Group13_Articulated_2024/assets/157665975/0836528d-49da-4a64-ab87-37b3838f418e" alt="Discussion of Kinematic Diagram and D-H Frame for the Articulated Manipulator" width = 600 title="Discussion of Kinematic Diagram and D-H Frame for the Articulated Manipulator">
      
## <h2 align="center">IV. D-H PARAMETRIC TABLE


## <h2 align="center">V. HOMOGENEOUS TRANSFORMATION MATRIX


## <h2 align="center">VI. INVERSE KINEMATICS USING GRAPHICAL METHOD

## <h2 align="center">VII. FORWARD AND INVERSE KINEMATICS GUI CALCULATOR

## <h2 align="center">VIII. REFERENCES

## <h2 align="center">Our Team 

<h2 align="left">Abong, Louwella (PL)
  
  Atienza, Ma. Angela (PQ)
  
  Marasigan, Stanlee (PP)
  
  Reyes, Shervin (PS)

<h2 align="center">Our Team 
Abong, Louwella (PL)
  
Atienza, Ma. Angela (PQ)

Marasigan, Stanlee (PP)

Reyes, Shervin (PS)
