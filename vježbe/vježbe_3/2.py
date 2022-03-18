import particle as prt
import numpy as np
import matplotlib.pyplot as plt


#error funkcija
def err(num, an):
    return 100*np.abs((num-an)/an)

dt = 1e-5 #početni dt
t = [] #lista dt-ova
error = [] #lista errora

p1 = prt.Particle()

while(dt<0.12):
    p1.set_initial_conditions(10, 60, 0, 0, dt)
    if(len(t)==0): #analitičko rješenje
        an_sol = p1.v_0**2/9.81*np.sin(2*p1.th)
    num_sol = p1.range()
    error += [err(num_sol, an_sol)]
    t += [dt]
    p1.reset()
    dt += 1e-3

#plotanje
plt.plot(t, error)
plt.xlabel("dt[s]")
plt.ylabel("Absolute relative error [%]")
plt.show()