### Inverse Kinematics Using Graphical Method of ARTICULATED MANIPULATOR
import numpy as np

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# Position vector in mm
x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))

if x0_3 == 0:
    theta1 = np.pi/2 if y0_3 > 0 else -np.pi/2
else:
    theta1 = np.arctan(y0_3/x0_3) #Solution1


r1 = np.sqrt(y0_3**2 + x0_3**2) #Solution2
r2 = z0_3-a1 #Solution3

if r1 == 0:
    phi1 = np.pi/2 if r2 > 0 else - np.pi/2
else:
    phi1 = np.arctan(r2/r1) #Solution4

r3 = np.sqrt(r2**2+r1**2) #Solution5

phi2 = np.arccos(np.clip((a3**2-a2**2-r3**2)/(-2*a2*r3),-1,1)) #Solution6

theta2 = phi1+phi2 #Solution7

phi3 = np.arccos(np.clip((r3**2-a2**2-a3**2)/(-2*a2*a3),-1,1)) #Solution8

theta3 = phi3-np.pi #Solution9

print("theta1 = ", np.around(theta1*180/np.pi,3))
print("theta2 = ", np.around(theta2*180/np.pi,3))
print("theta3 = ", np.around(theta3*180/np.pi,3))