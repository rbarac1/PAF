import bungee as bu
import matplotlib.pyplot as plt

p1 = bu.bungee(1,2,1,90,90,10) #(ro, Cd, A, m, k, l)

(t,y) = p1.jump(T=80)

plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.plot(t,y, label="dt=0.01 Runge-Kutta") #y-os je okrenuta prema dolje
plt.title("y-t graf", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)
plt.legend()


plt.subplot(1,2,2)

(Ek, Eg, Eel, Etot) = (p1.E_k(),p1.E_g(),p1.E_el(),p1.E_tot())

plt.plot(t,Ek, label="kinetic energy", c="orange")
plt.plot(t,Eg, label="gravitational pot. energy", c="green")
plt.plot(t,Eel, label="elastic pot. energy", c="red")
plt.plot(t,Etot, label="total energy", c="violet")

plt.title("Energy conservation", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel("E[J]", fontsize=14)
plt.legend()

plt.tight_layout()
plt.show()