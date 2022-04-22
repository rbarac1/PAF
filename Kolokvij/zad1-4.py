import numpy as np
import matplotlib.pyplot as plt
import projectile_drop as pd

###########################################
#   ZADATAK 1

p1 = pd.ProjectileDrop(2,200) #visina u km, brzina u m/s
p2 = pd.ProjectileDrop(5,500)

print("\n")


##########################################
#   ZADATAK 2

#1. objekt
p1.set_height(3)
p1.add_hvelocity(15)
print("")

#2. objekt
p2.set_height(4)
p2.add_hvelocity(-103)
print("\n")


##########################################
#   ZADATAK 3

p1 = pd.ProjectileDrop(2,200)

(dt, t, x, y, vy) = p1.drop()

plt.figure(figsize=(12,6))

plt.suptitle("Zadatak 3 dt={}s".format(dt), fontsize=16)

plt.subplot(1,2,1)  #x-t
plt.plot(x,y, "b")
plt.title("x-y graf", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)

plt.subplot(1,2,2)  #v-t
plt.plot(t,vy, "b")
plt.title("$\mathrm{v_y}$-t graf", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel(r"$\mathrm{v_y[\frac{m}{s}}$]", fontsize=14)

plt.show()


##########################################
#   ZADATAK 4

dts = np.linspace(0.001, 0.01, 100)
Tnum = [] 

for dt in dts:
    Tnum += [p1.num_T(dt)]

plt.scatter(dts, Tnum)
plt.title("Zadatak 4", fontsize=14)
plt.xlabel("T[s]", fontsize=14)
plt.ylabel("dt[s]", fontsize=14)
plt.xlim([dts[0], dts[-1]])
plt.tight_layout()
plt.show()
