import universe
import numpy as np
import matplotlib.pyplot as plt

sun = universe.Cobject(333000,0,0,0,0)
earth = universe.Cobject(1,1,0,0,2*np.pi)

ss = universe.Universe()
ss.addobject(sun)
ss.addobject(earth)

ss.evolve(1)    #1 year
#ss.evolve(1)    #1 year

fig = plt.figure(figsize=(10,10))
plt.plot(sun.r[:,0],sun.r[:,1], c="yellow", label='_nolegend_')
plt.plot(earth.r[:,0],earth.r[:,1], c="blue", label='_nolegend_')
plt.scatter(sun.r[-1,0],sun.r[-1,1], c="yellow", s=300, label="Sun")
plt.scatter(earth.r[-1,0],earth.r[-1,1], c="blue", label="Earth")
plt.xlabel("x[AU]", fontsize=14)
plt.ylabel("y[AU]", fontsize=14)
plt.title("x-y plane, dt={}yr, t={}yr".format(ss.dt, np.round(ss.t[-1], 2)), fontsize=14)
plt.axis("equal")
plt.legend()
plt.show()