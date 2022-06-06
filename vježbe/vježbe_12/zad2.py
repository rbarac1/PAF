import universe
import numpy as np
import matplotlib.pyplot as plt

#https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html
#pretpostavljamo da su sve orbite kružne
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

step = 50   #za koliko dt se razlikuju susjedni frameovi
for i in range (0, len(ss.t)-step+1,step):
    plt.xlim(-2,2)
    plt.ylim(-2,2)

    plt.plot(sun.r[i:i+step+1,0],sun.r[i:i+step+1,1], c="gold", label='_nolegend_')
    plt.plot(mercury.r[i:i+step+1,0],mercury.r[i:i+step+1,1], c="dimgray", label='_nolegend_')
    plt.plot(venus.r[i:i+step+1,0],venus.r[i:i+step+1,1], c="goldenrod", label='_nolegend_')
    plt.plot(earth.r[i:i+step+1,0],earth.r[i:i+step+1,1], c="blue", label='_nolegend_')
    plt.plot(mars.r[i:i+step+1,0],mars.r[i:i+step+1,1], c="orangered", label='_nolegend_')

    temp1 = plt.scatter(sun.r[i+step,0],sun.r[i+step,1], c="gold", s=450, label="Sun")
    temp2 = plt.scatter(mercury.r[i+step,0],mercury.r[i+step,1], c="dimgray", s=38, label='Mercury')
    temp3 = plt.scatter(venus.r[i+step,0],venus.r[i+step,1], c="goldenrod", s=95, label='Venus')
    temp4 = plt.scatter(earth.r[i+step,0],earth.r[i+step,1], c="blue", s=100, label="Earth")
    temp5 = plt.scatter(mars.r[i+step,0],mars.r[i+step,1], c="orangered", s=53, label='Mars')
    
    plt.legend()
    plt.xlabel("x[AU]", fontsize=14)
    plt.ylabel("y[AU]", fontsize=14)
    plt.title("x-y plane, dt={:}yr, t={:.2f}yr".format(ss.dt, np.round(ss.t[i+step], 2)), fontsize=14)
    
    plt.pause(0.001)

    temp1.remove()
    temp2.remove()
    temp3.remove()
    temp4.remove()
    temp5.remove()


plt.show()