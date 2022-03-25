import numpy as np
import matplotlib.pyplot as plt
import calculus as calc


def kub(x): #x^3
    return x*x*x

def derkub(x): #derivacija od x^3
    return 3*x*x


a = 2 #početak intervala derivacije
b = 4 #kraj intervala derivacije
dx = 1e-2 #minimalni korak, idući je 10 puta veći, a posljednji je 100 puta veći

xan = np.linspace(a,b)


plt.figure(figsize=(13,7))


#plotanje derivacije x^3
plt.subplot(1, 2, 1)
plt.plot(xan, derkub(xan), lw=2., label=r"analitčko rj.")
plt.title(r"derivacija od $\mathrm{x^3}$", fontsize=14)
plt.xlabel("x", fontsize=14)
plt.ylabel(r"$\mathrm{\frac{d}{dx}x^3}$", fontsize=14)

for i in range(3): #koristi se minimalni korak i svaki idući je 10 puta veći
    (xnum, dernum) = calc.met2(kub, a, b, dx*10**i) #za two-step metodu dodajte ,met=2 (default je three-step)
    plt.plot(xnum, dernum, ls='--', label="numeričko rj., dx = {}".format(dx*10**i))

plt.legend()



#plotanje derivacije sin(x)
plt.subplot(1, 2, 2)
plt.plot(xan, np.cos(xan), lw=2., label="analitčko rj.")
plt.title(r"derivacija od $\mathrm{\sin(x)}$", fontsize=14)
plt.xlabel("x", fontsize=14)
plt.ylabel(r"$\mathrm{\frac{d}{dx}\sin(x)}$", fontsize=14)



for i in range(3): #isto kao iznad
    (xnum, dernum) = calc.met2(np.sin, a, b, dx*10**i) #za two-step metodu dodajte ,met=2, default je three-step
    plt.plot(xnum, dernum, ls='--', label="numeričko rj., dx = {}".format(dx*10**i))

plt.legend()
plt.tight_layout()
plt.show()