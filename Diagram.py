import sys
sys.path.insert(0, "./codes/CoordGeo")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

def pointsOfContact(I, A, r):
    P = A-I
    d = math.sqrt(P[0]*P[0]+P[1]*P[1])
    theta = math.acos(r/d)
    phi = math.atan(P[1]/P[0])
    theta1 = phi + theta
    theta2 = phi - theta
    x1 = r*(math.cos(theta1))
    x2 = r*(math.cos(theta2))
    y1 = r*(math.sin(theta1))
    y2 = r*(math.sin(theta2))
    
    P1 = I + np.array([x1, y1])
    P2 = I + np.array([x2, y2])

    return P1, P2


A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])

x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)

[E3, F3] = pointsOfContact(I, A, r)


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(x_icirc[0,:],x_icirc[1,:],label='$incircle$')

tri_coords = np.vstack((A,B,C,E3, F3,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','E3', 'F3','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center') 


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.savefig('./Diagram.png')






