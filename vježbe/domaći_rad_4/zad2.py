import matplotlib.pyplot as plt
import numpy as np
import Projectile as pr

plt.figure(figsize=(13,6))


#1. meta
plt.subplot(2,2,1)
p1 = pr.projectile(15,1,1,1,1, dt=0.001)
(xm, ym, r) = (1,1,0.1)
p1.set_target(xm, ym, r)
(th,x,y) = p1.hit_target()

plt.plot(x,y, color="b")
circle1 = plt.Circle((xm, ym), r, color="r")
plt.gca().add_patch(circle1)
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.axis("equal")


#2. meta
plt.subplot(2,2,2)
p1 = pr.projectile(40,1,1,1,1, dt=0.001)
(xm, ym, r) = (-4, 3,1)
p1.set_target(xm, ym, r)
(th,x,y) = p1.hit_target()

plt.plot(x,y, color="b")
circle1 = plt.Circle((xm, ym), r, color="r")
plt.gca().add_patch(circle1)
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.axis("equal")


#3. meta
plt.subplot(2,2,3)
p1 = pr.projectile(10,1,1,1,1, dt=0.001)
(xm, ym, r) = (2,-1,0.15)
p1.set_target(xm, ym, r)
(th,x,y) = p1.hit_target()

plt.plot(x,y, color="b")
circle1 = plt.Circle((xm, ym), r, color="r")
plt.gca().add_patch(circle1)
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.axis("equal")


#4. meta
plt.subplot(2,2,4)
p1 = pr.projectile(30,1,1,1,1, dt=0.001)
(xm, ym, r) = (5,2,0.2)
p1.set_target(xm, ym, r)
(th,x,y) = p1.hit_target()

plt.plot(x,y, color="b")
circle1 = plt.Circle((xm, ym), r, color="r")
plt.gca().add_patch(circle1)
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.axis("equal")

plt.tight_layout()
plt.show()


