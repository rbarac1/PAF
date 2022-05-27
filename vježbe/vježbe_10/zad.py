import numpy as np
import charged_particle as cp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

B = 1
T = 20

pos = cp.qp(1,1,[0.1,0.1,0.1],[0,0,0],[0,0,B])
el = cp.qp(-1,1,[0.1,0.1,0.1],[0,0,0],[0,0,B])

r1 = pos.motion(T) #RK4
r2 = el.motion(T) #RK4

x1 = r1[:,0]
y1 = r1[:,1]
z1 = r1[:,2]

x2 = r2[:,0]
y2 = r2[:,1]
z2 = r2[:,2]

pos.reset()
el.reset()

r3 = pos.motion(T, method="Euler")
r4 = el.motion(T, method="Euler")

x3 = r3[:,0]
y3 = r3[:,1]
z3 = r3[:,2]

x4 = r4[:,0]
y4 = r4[:,1]
z4 = r4[:,2]


fig = plt.figure(figsize=(11,9))

ax = fig.add_subplot(111, projection='3d')
ax.plot(x1,y1,z1, c="r", label="Positron - RK4")
ax.plot(x2,y2,z2, c="b", label="Electron - RK4")
ax.plot(x3,y3,z3, "r--", label="Positron - Euler")
ax.plot(x4,y4,z4, "b--", label="Electron - Euler")
ax.set_title(r"$\mathrm{m=1, q=\pm1, \vec{B}=1\hat{k}, \vec{v_0}=(0.1,0.1,0.1), dt=0.01}$", fontsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()

###########ZADATAK 1###########
#Eleketron i pozitron imaju spiralnu putanju (helix) i okreću se u suprotnim smjerovima.

###########ZADATAK 2###########
#Kod Euler-ove metode se iznos vektora brzine prebrzo mijenja pa se čestice ne gibaju po kružnici u xy ravnini.
#Razlog je što u analitičkom rješenju okomiti diferencijal brzine samo promijeni smjer brzine (sin(x)=x), a ovdje delta t nije diferencijal pa mijenja i iznos (u ovom slučaju ga smanjuje).