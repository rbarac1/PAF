import universe
import numpy as np
import matplotlib.pyplot as plt

#https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html

sun = universe.Cobject(333000,0,0,0,0)
earth = universe.Cobject(1,1,0,0,2*np.pi)
mercury = universe.Cobject(0.0553,0.387,0,0,2*np.pi*1.59)
venus = universe.Cobject(0.815,0.723,0,0,2*np.pi*1.18)
mars = universe.Cobject(0.107,1.52,0,0,2*np.pi*0.808)

ss = universe.Universe()
ss.addobject(sun)
ss.addobject(earth)
ss.addobject(mercury)
ss.addobject(venus)
ss.addobject(mars)

ss.evolve(5)    #5 years

fig = plt.figure(figsize=(10,10))

plt.plot(sun.r[:,0],sun.r[:,1], c="gold", label='_nolegend_')
plt.plot(mercury.r[:,0],mercury.r[:,1], c="dimgray", label='_nolegend_')
plt.plot(venus.r[:,0],venus.r[:,1], c="goldenrod", label='_nolegend_')
plt.plot(earth.r[:,0],earth.r[:,1], c="blue", label='_nolegend_')
plt.plot(mars.r[:,0],mars.r[:,1], c="orangered", label='_nolegend_')

plt.scatter(sun.r[-1,0],sun.r[-1,1], c="gold", s=450, label="Sun")
plt.scatter(mercury.r[-1,0],mercury.r[-1,1], c="dimgray", s=38, label='Mercury')
plt.scatter(venus.r[-1,0],venus.r[-1,1], c="goldenrod", s=95, label='Venus')
plt.scatter(earth.r[-1,0],earth.r[-1,1], c="blue", s=100, label="Earth")
plt.scatter(mars.r[-1,0],mars.r[-1,1], c="orangered", s=53, label='Mars')

plt.xlabel("x[AU]", fontsize=14)
plt.ylabel("y[AU]", fontsize=14)
plt.title("x-y plane, dt={}yr, t={}yr".format(ss.dt, np.round(ss.t[-1], 2)), fontsize=14)
plt.axis("equal")
plt.legend()
plt.show()