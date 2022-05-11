import matplotlib.pyplot as plt
import Projectile as pr

p1 = pr.projectile(10,60,1,1,0.1,1,dt=0.01)

(x,y) = p1.motion(method="Euler")

plt.figure(figsize=(11,8))
plt.plot(x,y)
plt.title("x-y graf Eulerova metoda", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)
plt.tight_layout()
plt.show()


###Za duže vrijeme gibanja dt mora biti veći, a za kraće vrijeme gibanja kraći.
###Za zadane uvjete je dt=0.01 dovoljan