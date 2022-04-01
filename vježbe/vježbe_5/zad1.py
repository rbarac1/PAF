import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as ho


h1 = ho.HarmonicOscillator()
h1.init(0.1, 10, 0.3, 0) #(m, k, x0, v0) početni uvjeti
#h1.oscillate(2) #oscilacija od 2s
#h1.plot_trajectory() #plotanje samo numeričkih rješenja

plt.figure(figsize=(12,7))

dts = [0.001, 0.01, 0.05] #vremenski intervali za num. rješenja
colors = ["blue", "orange", "green"] #boje točkica
sizes = [9, 18, 30] #veličine točkica

for i in range(3):
    h1.reset() #vraćanje gibanja na početak sa zadnjim zadanim početnim uvjetima
    h1.oscillate(1.6, dt=dts[i]) #1.6s oscilacija
    h1.oscillate(0.4, dt=dts[i]) #0.4s oscilacija
    (tnum, xnum, vnum, anum, tan, xan, van, aan) = h1.plot_trajectory(plot="hide", t0=0) #plotam oscilacije od trenutka t0 do kraja

    plt.subplot(1, 3, 1)    #x-t plot
    plt.scatter(tnum, xnum, c=colors[i], s=sizes[i], label="dt={}".format(np.round(dts[i], 3 if i==0 else 2)))

    plt.subplot(1, 3, 2)    #v-t plot
    plt.scatter(tnum, vnum, c=colors[i], s=sizes[i], label="dt={}".format(np.round(dts[i], 3 if i==0 else 2)))

    plt.subplot(1, 3, 3)    #a-t plot
    plt.scatter(tnum, anum, c=colors[i], s=sizes[i], label="dt={}".format(np.round(dts[i], 3 if i==0 else 2)))



#x-t graf
plt.subplot(1,3,1)
plt.plot(tan, xan, c="r", lw = 1.3, label="analitičko rješenje")
plt.title("x-t graf", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel("x[m]", fontsize=14)
plt.legend()

#v-t graf
plt.subplot(1,3,2)
plt.plot(tan, van, c="r", lw = 1.3, label="analitičko rješenje")
plt.title("v-t graf", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel(r"v$\mathrm{\frac{m}{s}}$", fontsize=14)
plt.legend()

#a-t graf
plt.subplot(1,3,3)
plt.plot(tan, aan, c="r", lw = 1.3, label="analitičko rješenje")
plt.title("a-t graf", fontsize=14)
plt.xlabel("t[s]", fontsize=14)
plt.ylabel(r"a$\mathrm{\frac{m}{s^2}}$", fontsize=14)
plt.legend()

#prikaz na ekranu
plt.tight_layout()
plt.show()