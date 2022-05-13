from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import Projectile as pr

plt.figure(figsize=(13,6))
#gledam 3 različita slučaja (početni uvjeti)

#kocka
plt.subplot(1,3,1)
v0 = 30
th = 89
p1 = pr.projectile(v0,1,1,1,1,"cube",th, dt=0.001) #(v0, ro, Cd, m, duljina brida, "oblik", kut ispaljivanja)
(x,y) = p1.motion()
plt.plot(x,y, c="blue", label="kocka")

#stavit ću kuglu iste mase i volumena radi bolje usporedbe
p2 = pr.projectile(v0,1,1,1,(3/(4*np.pi))**(1/3),"sphere",th, dt=0.001) #(v0, ro, Cd, m, radijus, "oblik", kut ispaljivanja)
(x,y) = p2.motion()
plt.plot(x,y, c="red", label="kugla")


plt.title(r"$\mathrm{v_0}$" + "={}m/s".format(v0) + r"$\mathrm{, \theta_0}$" + "={}".format(th) + r"$^{\circ}$", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)
plt.legend()


#kocka
plt.subplot(1,3,2)
v0 = 30
th = 45
p1 = pr.projectile(v0,1,1,1,1,"cube",th, dt=0.001) #(v0, ro, Cd, m, duljina brida, "oblik", kut ispaljivanja)
(x,y) = p1.motion()
plt.plot(x,y, c="blue", label="kocka")

#stavit ću kuglu iste mase i volumena radi bolje usporedbe
p2 = pr.projectile(v0,1,1,1,(3/(4*np.pi))**(1/3),"sphere",th, dt=0.001) #(v0, ro, Cd, m, radijus, "oblik", kut ispaljivanja)
(x,y) = p2.motion()
plt.plot(x,y, c="red", label="kugla")


plt.title(r"$\mathrm{v_0}$" + "={}m/s".format(v0) + r"$\mathrm{, \theta_0}$" + "={}".format(th) + r"$^{\circ}$", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)
plt.legend()


#kocka
plt.subplot(1,3,3)
v0 = 30
th = 1
p1 = pr.projectile(v0,1,1,1,1,"cube",th, dt=0.001) #(v0, ro, Cd, m, duljina brida, "oblik", kut ispaljivanja)
(x,y) = p1.motion()
plt.plot(x,y, c="blue", label="kocka")

#stavit ću kuglu iste mase i volumena radi bolje usporedbe
p2 = pr.projectile(v0,1,1,1,(3/(4*np.pi))**(1/3),"sphere",th, dt=0.001) #(v0, ro, Cd, m, radijus, "oblik", kut ispaljivanja)
(x,y) = p2.motion()
plt.plot(x,y, c="red", label="kugla")


plt.title(r"$\mathrm{v_0}$" + "={}m/s".format(v0) + r"$\mathrm{, \theta_0}$" + "={}".format(th) + r"$^{\circ}$", fontsize=14)
plt.xlabel("x[m]", fontsize=14)
plt.ylabel("y[m]", fontsize=14)
plt.legend()

plt.tight_layout()
plt.show()

#ako uzmemo kuglu i kocku istog volumena, minimalni poprečni presjek kocke je manji od poprečnog presjeka kugle,
#a maksimalni poprečni presjek kocke je veći od poprečnog presjeka kugle
#poprečni presjek kocke je najmanji kad se kocka giba paralelno sa nekim svojim bridovima (u ovom slučaju po koordinatnim osima)
#poprečni presjek kocke je najveći kad se kocka giba u dijagonalnom smjeru (iznos vx= iznos vy)
#rezultat ovoga je da se kocka giba brže od kugle kad smo blizu horizontalnog ili vertikalnog hica (kocka tada više vremena provodi u položaju manjeg otpora)