import numpy as np
import math

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# joint variables: is mm if f, is degrees is theta
T1 = float(input("T1 = "))
T2 = float(input("T2 = "))
T3 = float(input("T3 = "))

# degree to radian

T1 = (T1/160.0)*np.pi
T2 = (T2/180.0)*np.pi
T3 = (T3/180.0)*np.pi

# Parametric Table (theta, alpha, r, d)
PT = [[T1,(90.0/180.0)*np.pi,0,a1],
      [T2,(0.0/180.0)*np.pi,a2,0],
      [T3,(0.0/180.0)*np.pi,a3,0]]

# HTM formulae
i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

H0_1 = np.matrix (H0_1)

H1_2 = np.matrix (H1_2)

H2_3 = np.matrix (H2_3)


H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)

x0_3 = H0_3[0,3]
print("x0_3 = ")
print(np.around(x0_3,3))

y0_3 = H0_3[1,3]
print("y0_3 = ")
print(np.around(y0_3,3))

z0_3 = H0_3[2,3]
print("z0_3 = ")
print(np.around(z0_3,3))
