import matplotlib.pyplot as plt
import numpy as np
import Projectile as pr


plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
Cds = np.linspace(0.5,5,20) #Koeficijent trenja
Cd_range = []

for Cd in Cds:
    p1 = pr.projectile(10,60,1,Cd,0.1,1,dt=0.006)
    Cd_range += [p1.range()]


plt.plot(Cds,Cd_range)
plt.title("Ovisnost dometa o koeficijentu trenja", fontsize=14)
plt.xlabel(r"$\mathrm{C_D}$", fontsize=14)
plt.ylabel("domet[m]", fontsize=14)



plt.subplot(1,2,2)
ms = np.linspace(0.5,5,20) #masa
m_range = []

for m in ms:
    p1 = pr.projectile(10,60,1,1,0.1,m,dt=0.0015)
    m_range += [p1.range()]


plt.plot(ms,m_range)
plt.title("Ovisnost dometa o masi projektila", fontsize=14)
plt.xlabel("m[kg]", fontsize=14)
plt.ylabel("domet[m]", fontsize=14)


plt.tight_layout()
plt.show()

#Domet je manji što je koeficijent trenja veći.
#Domet je veći što je masa veća.