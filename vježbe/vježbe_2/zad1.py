import numpy as np
import matplotlib.pyplot as plt

T = 10. #vrijeme gibanja u sekundama

F = 10. #iznos sile u newtonima
m = 5. #masa čestice u kg

v = [0.] #početna brzina
x = [0.] #početni položaj

a = F/m #akceleracija

N = 1e5 #broj koraka pri numeričkom riješavanju

dt = T/N #vremenska razlika između koraka

N = int(N)

#numeričko računanje brzine i položaja
for i in range(N):
    v += [v[i]+a*dt]
    x += [x[i]+v[i+1]*dt]

t = np.linspace(0, T, N+1)

fig, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(7,10))

#graf položaja
ax1.plot(t,x)
ax1.title.set_text('Položaj')
ax1.set_xlabel(r'$t[s]$')
ax1.set_ylabel(r'$x[m]$')

#graf brzine
ax2.plot(t,v)
ax2.title.set_text('Brzina')
ax2.set_xlabel(r'$t[s]$')
ax2.set_ylabel(r'$v[m/s]$')

#graf akceleracije
ax3.plot(t,len(t)*[a])
ax3.title.set_text('Akceleracija')
ax3.set_xlabel(r'$t[s]$')
ax3.set_ylabel(r'$a[m/s^2]$')

#plotanje
plt.tight_layout()
plt.show()