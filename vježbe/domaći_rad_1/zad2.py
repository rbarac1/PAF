import particle as prt
import numpy as np
import matplotlib.pyplot as plt

ang = np.linspace(0,90) #raspon kuta ispaljivanja projektila u stupnjevima

p1 = prt.Particle()

v0 = 12 #početna brzina
d = [] #lista dometa
t = [] #lista vremena trajanja gibanja

for i in ang: #računanje dometa i vremena gibanja
    p1.set_initial_conditions(v0, i, 0., 0.)
    t += [p1.total_time()]
    p1.set_initial_conditions(v0, i, 0., 0.)
    d += [p1.range()]


plt.figure(figsize=(13,7))

#plotanje dometa
plt.subplot(1, 2, 1)
plt.plot(ang, d)
plt.title("Domet", fontsize=14)
plt.xlabel(r"$\mathrm{kut[\degree]}$", fontsize=14)
plt.ylabel("d[m]", fontsize=14)

#plotanje vremena trajanja gibanja
plt.subplot(1, 2, 2)
plt.plot(ang, t)
plt.title("Vrijeme trajanja gibanja", fontsize=14)
plt.xlabel(r"$\mathrm{kut[\degree]}$", fontsize=14)
plt.ylabel("t[s]", fontsize=14)

plt.show() #prikaz plota na ekranu