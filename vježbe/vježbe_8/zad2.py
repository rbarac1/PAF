import matplotlib.pyplot as plt
import Projectile as pr

p1 = pr.projectile(1000,60,1,1,0.2,1,dt=0.01)


plt.figure(figsize=(14,8))
plt.subplot(1,3,1)
(x,y) = p1.motion(method="Euler")
plt.plot(x,y)
plt.title("x-y graf Eulerova metoda dt=0.01", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)

plt.subplot(1,3,2)
p1.reset()
(x,y) = p1.motion(method="RK4")
plt.plot(x,y)
plt.title("x-y graf RK4 metoda dt=0.01", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)


p1 = pr.projectile(1000,60,1,1,0.2,1,dt=0.0001)
plt.subplot(1,3,3)
(x,y) = p1.motion(method="Euler")
plt.plot(x,y)
plt.title("x-y graf Eulerova metoda dt=0.001", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)


plt.tight_layout()
plt.show()

##Dodao sam Eulerovu metodu sa većom preciznosti da se uvjerim da je RK4 metoda točna.
##RK4 metoda daje precizan rezultat, dok Eulerova pokazuje nefizikalno ponašanje.
##Kod Eulerove metode postoji nekakva točka infleksije u putanji, dok je pri RK4 metodi nema