import tkinter as tk
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import matplotlib
matplotlib.use('TkAgg')

#Create GUI Window with title
gggui = Tk()
gggui.title('Articulated Calculator')
gggui.resizable(False,False)
gggui.configure(bg='Navy')


def reset():
    a1_E.delete(0,END)
    a2_E.delete(0,END)
    a3_E.delete(0,END)

    T1_E.delete(0,END)
    T2_E.delete(0,END)
    T3_E.delete(0,END)

    Z_E.delete(0,END)
    Y_E.delete(0,END)
    X_E.delete(0,END)

def f_k():
#link lengths in mm
    a1 = float(a1_E.get())/100
    a2 = float(a2_E.get())/100
    a3 = float(a3_E.get())/100

#joint variables in mm
    T1 = float(T1_E.get())
    T2 = float(T2_E.get())
    T3 = float(T3_E.get())

# degree to radian
    T1 = (T1/180.0)*np.pi
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

    X0_3 = H0_3[0,3]
    X_E.delete(0,END)
    X_E.insert(0,np.around(X0_3*100,3))

    Y0_3 = H0_3[1,3]
    Y_E.delete(0,END)
    Y_E.insert(0,np.around(Y0_3*100,3))

    Z0_3 = H0_3[2,3]
    Z_E.delete(0,END)
    Z_E.insert(0,np.around(Z0_3*100,3))

#Create links
#[robot_value]=DHRobot([RevoluteDH(d,r,alpha,offset)])

    Articulated = DHRobot([
        RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])],name='Articulated')

    q1 = np.array([T1,T2,T3])
    
        #plot scale
        x1 = -0.5
        x2 = 0.5
        y1 = -0.5
        y2 = 0.5
        z1 = 0.0
        z2 = 0.5
    
        #Plot Command
        Articulated.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

def i_k():
#link lengths in mm
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())

#position vector in mm
    x0_3 = float(X_E.get())
    y0_3 = float(Y_E.get())
    z0_3 = float(Z_E.get())

    if x0_3 == 0:
         t1 = np.pi/2 if y0_3 > 0 else -np.pi/2
    else:
         t1 = np.arctan(y0_3/x0_3) #Solution1

    r1 = np.sqrt(y0_3**2 + x0_3**2) #Solution2
    r2 = z0_3-a1 #Solution3

    if r1 == 0:
         phi1 = np.pi/2 if r2 > 0 else - np.pi/2
    else:
         phi1 = np.arctan(r2/r1) #Solution4

    r3 = np.sqrt(r2**2+r1**2) #Solution5

    phi2 = np.arccos(np.clip((a3**2-a2**2-r3**2)/(-2*a2*r3),-1,1)) #Solution6

    t2 = phi1+phi2 #Solution7

    phi3 = np.arccos(np.clip((r3**2-a2**2-a3**2)/(-2*a2*a3),-1,1)) #Solution8

    t3 = phi3-np.pi #Solution9

    T1_E.delete(0,END)
    T1_E.insert(0,np.around(t1*180/np.pi,3))

    T2_E.delete(0,END)
    T2_E.insert(0,np.around(t2*180/np.pi,3))

    T3_E.delete(0,END)
    T3_E.insert(0,np.around(t3*180/np.pi,3))

#Create links
#[robot_value]=DHRobot([RevoluteDH(d,r,alpha,offset)])

    Articulated = DHRobot([
        RevoluteDH(a1/100,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2/100,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3/100,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])],name='Articulated')
   
    q1 = np.array([Th1,Th2,Th3])
    
        #plot scale
        x1 = -0.5
        x2 = 0.5
        y1 = -0.5
        y2 = 0.5
        z1 = 0.0
        z2 = 0.5
    
        #Plot Command
        Articulated.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)


    print(Articulated)
#Link lengths and Joint Variable Frame
FI=LabelFrame(gggui,text='Link Lengths and Joint Variables',padx=15,pady=15,relief="solid",font=('Times New Roman', 12,'bold'),bd=3,bg='Lightblue')
FI.grid(row=0,column=0,padx=10, pady=5)

#Link Lenghts Label
a1 = Label(FI,text=('a1='),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
a1_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
mm1 =  Label(FI,text=('mm'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

a2 = Label(FI,text=('a2='),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
a2_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
mm2 =  Label(FI,text=('mm'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

a3 = Label(FI,text=('a3='),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
a3_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
mm3 =  Label(FI,text=('mm'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

a1.grid(row=0,column=0,padx=5)
a1_E.grid(row=0,column=1)
mm1.grid(row=0,column=2,)

a2.grid(row=1,column=0,padx=5)
a2_E.grid(row=1,column=1)
mm2.grid(row=1,column=2)

a3.grid(row=2,column=0,padx=5)
a3_E.grid(row=2,column=1)
mm3.grid(row=2,column=2)

#Joint Variable Label
T1 = Label(FI,text=('T1 = '),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
T1_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
deg1 = Label(FI,text=('deg'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

T2 = Label(FI,text=('T2 = '),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
T2_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
deg2 = Label(FI,text=('deg'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

T3 = Label(FI,text=('T3 = '),padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
T3_E = Entry(FI,width=8,font=('Times New Roman', 12),bg='#E9C46A')
deg3 = Label(FI,text=('deg'),font=('Times New Roman', 12,'bold'),bg='#2A9D8F')

T1.grid(row=0,column=3,padx=5)
T1_E.grid(row=0,column=4)
deg1.grid(row=0,column=5)

T2.grid(row=1,column=3,padx=5)
T2_E.grid(row=1,column=4)
deg2.grid(row=1,column=5)

T3.grid(row=2,column=3,padx=5)
T3_E.grid(row=2,column=4)
deg3.grid(row=2,column=5)

#Buttons Frame
BF = LabelFrame(gggui,text='Forward Kinematics',padx=10,pady=10,relief="solid",font=('Times New Roman',12,'bold'),bd=3,bg='Lightblue')
BF.grid(row=1,column=0,padx=10,pady=5)

#Buttons
FK = Button(BF,text='Forward',padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='blue',fg='white',command=f_k)
rst = Button(BF,text='Reset',padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='red',fg='white',command=reset)
IK = Button(BF,text='Inverse',padx=5,pady=5,relief="solid",font=('Times New Roman', 12,'bold'),bg='green',fg='white',command=i_k)

FK.grid(row=0,column=0,padx=5)
rst.grid(row=0,column=1,padx=5)
IK.grid(row=0,column=2,padx=5)

#Position Vectors Frame
PV = LabelFrame(gggui,text='Position Vector',padx=10,pady=10,relief="solid",font=('Times New Roman',12,'bold'),bd=3,bg='Lightblue')
PV.grid(row=2,column=0,padx=10, pady=5)

#Position Vector Label
X = Label(PV,text=('X = '),padx=0,pady=0,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
X_E = Entry(PV,width=10,font=('Times New Roman', 12),bg='#E9C46A')
mm4 =  Label(PV,text=('mm'),padx=0,pady=0,relief="solid",font=('Times New Roman', 12),bg='#2A9D8F')

Y = Label(PV,text=('Y = '),padx=0,pady=0,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
Y_E = Entry(PV,width=10,font=('Times New Roman', 12),bg='#E9C46A')
mm5 =  Label(PV,text=('mm'),padx=0,pady=0,relief="solid",font=('Times New Roman', 12),bg='#2A9D8F')

Z = Label(PV,text=('Z = '),padx=0,pady=0,relief="solid",font=('Times New Roman', 12,'bold'),bg='#2A9D8F')
Z_E = Entry(PV,width=10,font=('Times New Roman', 12),bg='#E9C46A')
mm6 =  Label(PV,text=('mm'),padx=0,pady=0,relief="solid",font=('Times New Roman', 12),bg='#2A9D8F')

X.grid(row=0,column=0,padx=5)
X_E.grid(row=0,column=1)
mm4.grid(row=0,column=2)

Y.grid(row=1,column=0,padx=5)
Y_E.grid(row=1,column=1)
mm5.grid(row=1,column=2)

Z.grid(row=2,column=0,padx=5)
Z_E.grid(row=2,column=1)
mm6.grid(row=2,column=2)

#insert image
img = PhotoImage(file="articulated.png")
img = img.subsample(3,3)
PI = Label(gggui,image=img)
PI.grid(row=3,column=0,columnspan=5,padx=10,pady=5,sticky=NSEW)

  
gggui.mainloop()

 
