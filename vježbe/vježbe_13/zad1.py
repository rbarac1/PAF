import universe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def kg(x):  #kg u M_earth
    return x/(5.972e24)

def km(x):  #km u AU
    return x*6.68459e-9

def kms(x): #km/s u AU/year
    return x*6.68459e-9*3.156e+7

#https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html
#pretpostavljamo da su sve orbite kružne
sun = universe.Cobject(333000,0,0,0,0)
earth = universe.Cobject(1,1,0,0,2*np.pi)
mercury = universe.Cobject(0.0553,0.387,0,0,2*np.pi*1.59)
venus = universe.Cobject(0.815,0.723,0,0,2*np.pi*1.18)
mars = universe.Cobject(0.107,1.52,0,0,2*np.pi*0.808)
comet = universe.Cobject(kg(1e14),-5,3,kms(14),kms(-4))

ss = universe.Universe()
ss.addobject(sun)
ss.addobject(earth)
ss.addobject(mercury)
ss.addobject(venus)
ss.addobject(mars)
ss.addobject(comet)

ss.evolve(2.5, dt=0.005)    #5 years

fig = plt.figure(figsize=(10,10))

plt.xlim(-4,4)
plt.ylim(-4,4)

plt.xlabel("x[AU]", fontsize=14)
plt.ylabel("y[AU]", fontsize=14)

s0 = plt.scatter([],[], c="gold", s=450, label="Sun")
s1 = plt.scatter([],[], c="dimgray", s=38, label='Mercury')
s2 = plt.scatter([],[], c="goldenrod", s=95, label='Venus')
s3 = plt.scatter([],[], c="blue", s=100, label="Earth")
s4 = plt.scatter([],[], c="orangered", s=53, label='Mars')
s5 = plt.scatter([],[], c="black", s=33, label='Comet')

step = 4

plt.suptitle("Inner Solar System", y=0.95, fontsize=20)

def run(i):
    plt.title("x-y plane, dt={:}yr, t={:.2f}yr".format(ss.dt, np.round(ss.t[i], 2)), fontsize=14)

    s0.set_offsets([[sun.r[i, 0], sun.r[i, 1]]])
    s1.set_offsets([[mercury.r[i, 0], mercury.r[i, 1]]])
    s2.set_offsets([[venus.r[i, 0], venus.r[i, 1]]])
    s3.set_offsets([[earth.r[i, 0], earth.r[i, 1]]])
    s4.set_offsets([[mars.r[i, 0], mars.r[i, 1]]])
    s5.set_offsets([[comet.r[i, 0], comet.r[i, 1]]])

    plt.plot(sun.r[i-step:i+1, 0], sun.r[i-step:i+1, 1], c="gold", label='_nolegend_')
    plt.plot(mercury.r[i-step:i+1, 0], mercury.r[i-step:i+1, 1], c="dimgray", label='_nolegend_')
    plt.plot(venus.r[i-step:i+1, 0], venus.r[i-step:i+1, 1], c="goldenrod", label='_nolegend_')
    plt.plot(earth.r[i-step:i+1, 0], earth.r[i-step:i+1, 1], c="blue", label='_nolegend_')
    plt.plot(mars.r[i-step:i+1, 0], mars.r[i-step:i+1, 1], c="orangered", label='_nolegend_')
    plt.plot(comet.r[i-step:i+1, 0], comet.r[i-step:i+1, 1], c="black", label='_nolegend_')


ts = range(0,len(ss.t),step)
ani = animation.FuncAnimation(fig,run,ts,interval=2)

plt.legend()
plt.show()