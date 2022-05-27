import numpy as np
import charged_particle as cp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return 0.1*x

def const(x):
    return x


T = 10
q = 1 #mijenjanje naboja


pos = cp.qp(q,1,[0.1,0.1,0.1],[0,0,0],[0.,0.,0.], f)
el = cp.qp(-1*q,1,[0.1,0.1,0.1],[0,0,0],[0.,0.,0.], f)

r1 = pos.motion(T) #RK4
r2 = el.motion(T) #RK4

x1 = r1[:,0]
y1 = r1[:,1]
z1 = r1[:,2]

x2 = r2[:,0]
y2 = r2[:,1]
z2 = r2[:,2]


el.reset()
el.new_function(const)

r3 = el.motion(T, method="Euler")

x3 = r3[:,0]
y3 = r3[:,1]
z3 = r3[:,2]


fig = plt.figure(figsize=(11,9))

ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot(x2,y2,z2, "b", label="Promjenjivi B")
ax.plot(x3,y3,z3, "b--", label="Konstantni B")
ax.set_title("Eleketron u konstantnom i vremenski promjenjivom B", pad=50, fontsize=13)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)
ax.legend()

ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot(x1,y1,z1, c="r", label="Positron")
ax.plot(x2,y2,z2, c="b", label="Electron ")
ax.set_title("Pozitron i elektron u vremenski promjenjivom B", pad=50, fontsize=13)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)
ax.legend()


plt.tight_layout()
plt.show()
