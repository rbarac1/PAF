from re import T
import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as ho

h1 = ho.HarmonicOscillator()

m = 0.1 #masa
k = 10  #konstanta opruge
h1.init(m, k, 0.3, 0) #(m, k, x0, v0) početni uvjeti



dts = [0.001, 0.01, 0.05] #vremenski intervali za num. rješenja
colors = ["blue", "orange", "green"] #boje linija

plt.figure(figsize=(12,8))

for i in range(3):
    h1.reset() #vraćanje gibanja na početak sa zadnjim zadanim početnim uvjetima
    h1.oscillate(0.5, dt=dts[i]) #0.5s oscilacija
    (tnum, xnum, vnum, anum, tan, xan, van, aan) = h1.plot_trajectory(plot="hide")

    ii = 1
    j = []  #indeks prolaska kroz ishodište
    while len(j)<4:
        if ii==len(tnum): #još oscilacija ako je potrebno
            h1.oscillate(2, dt=dts[i]) #još 2s oscilacija
            (tnum, xnum, vnum, anum, tan, xan, van, aan) = h1.plot_trajectory(plot="hide")

        if(xnum[ii-1]*xnum[ii]<0): #prolazak kroz ishodište
            j += [ii]

        

        ii+=1

    T = tnum[j[2]]-tnum[j[0]] #period

    if i==2:
        Tmax = T

    plt.plot([0,1], [T,T], c=colors[i], label="dt={}".format(np.round(dts[i], 3 if i==0 else 2))) #num plot

#analitičko rješenje
Tan = 2*np.pi/np.sqrt(k/m)
plt.plot([0,1], [Tan,Tan], c="red", label="analitičko rješenje")

#informacije o grafu
plt.title("Period titranja", fontsize=14)
plt.ylabel("period[s]", fontsize=14)
plt.xlabel("vrijeme[s]", fontsize=14)
plt.legend()
plt.tight_layout()

#prikaz na ekranu
plt.show()