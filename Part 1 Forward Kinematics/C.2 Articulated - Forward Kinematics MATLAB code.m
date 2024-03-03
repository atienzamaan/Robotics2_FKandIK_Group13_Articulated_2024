% CLear
clear
clc
close

disp('Articulated')

syms a1 a2 a3 t1 t2 t3

%% Link Lengths
a1 = 10;
a2 = 30;
a3 = 10;

%% D-H Parameters [theta, d, r, alpha, offset]

H1 = Link([0,a1,0,pi/2,0]);
H1.qlim = [-pi/2 pi/2];

H2 = Link([0,0,a2,0,0]);
H2.qlim = [-pi/6 pi/2];

H3 = Link([0,0,a3,0,0]);
H3.qlim = [-pi/2 pi/2];

Articulated_1 = SerialLink([H1 H2 H3], 'name', 'Articulated');
Articulated_1.plot([0 0 0], 'workspace', [-50 50 -50 50 0 50])
Articulated_1.teach
