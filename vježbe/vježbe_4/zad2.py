import numpy as np
import matplotlib.pyplot as plt
import calculus as calc

#funkcija koju integriramo
def f(x):
    return 2*x*x+3

plt.figure(figsize=(12,7))

a = 0 #donja granica integracije
b = 1 #gornja granica integracije

for i in range(50, 1000, 50): #plotanje za različite korake
    plt.scatter(i, calc.pint(f, a, b, i)[0], c='r', s=10, label="gornja međa" if i==50 else"")
    plt.scatter(i, calc.pint(f, a, b, i)[1], c='b', s=10, label="donja međa" if i==50 else"")
    plt.scatter(i, calc.tint(f, a, b, i), c='green', s=10, label="trapezna integracija" if i==50 else"")

#analitičko rješenje za integral od 0 do 1 od 2*x*x+3
plt.axhline(y=11/3, color='lightblue', label="analitičko rješenje")

plt.legend()

#u naslovu grafa (red ispod) je funkcija koja je trenutno zadana, 2*x*x+3
plt.title(r"Numerička integracija: $\mathrm{\int_{0}^{1}2x^2+3\ dx}$")

plt.xlabel("N koraka")
plt.ylabel("vrijednost integrala")
plt.show()