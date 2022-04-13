import numpy as np
import matplotlib.pyplot as plt

import numerical_motion as nm


def fconst(v,x,t): #konstantna sila
    const = 2 #konstantna sila u newtonima
    return const


def ho(v,x,t): #harmonički oscilator
    k=2 #konstanta opruge [N/m]
    return -k*x


m = 1 #masa tijela u kg
tmax = 20 #vrijeme gibanja u sekundama




#provjera za konstantnu silu i harmonički oscilator (plot)
for i in range(2):
    if i:
        (t,x,v,a) = nm.move(ho, m, tmax, x0=5) #može se još dodati i x0, v0, t0 (default = 0) i dt(default=tmax/1000)

    else:
        (t,x,v,a) = nm.move(fconst, m, tmax) #može se još dodati i x0, v0, t0 (default = 0) i dt(default=tmax/1000)

    plt.figure(figsize=(12,6))

    plt.suptitle("Harmonički oscilator" if i else "Konstantna sila", fontsize=16)

    plt.subplot(1,3,1)  #x-t
    plt.plot(t,x, "b")
    plt.title("x-t graf", fontsize=14)
    plt.xlabel("t[s]", fontsize=14)
    plt.ylabel("x[m]", fontsize=14)

    plt.subplot(1,3,2)  #v-t
    plt.plot(t,v, "b")
    plt.title("v-t graf", fontsize=14)
    plt.xlabel("t[s]", fontsize=14)
    plt.ylabel(r"v[$\mathrm{\frac{m}{s}}$]", fontsize=14)

    plt.subplot(1,3,3)  #a-t
    plt.plot(t,a, "b")
    plt.title("a-t graf", fontsize=14)
    plt.xlabel("t[s]", fontsize=14)
    plt.ylabel(r"a[$\mathrm{\frac{m}{s^2}}]$", fontsize=14)

    plt.tight_layout()
    plt.subplots_adjust(top= 0.85)
    plt.show()