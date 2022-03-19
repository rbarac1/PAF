import numpy as np
import matplotlib.pyplot as plt


#funkcija koja plota putanju projektila dok ne udari tlo (y=0)
def khplot(v0, th):
    g = -9.81
    dt = 1e-5

    th = th*np.pi/180
    vx = v0*np.cos(th)
    vy = v0*np.sin(th)

    x = [0.]
    y = [0.]
    i = 0

    while y[i]>=0:
        x += [x[i]+vx*dt]
        y += [y[i]+vy*dt]

        vy += g*dt
        i += 1
    
    plt.plot(x,y)
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.show()
    

#funkcija koja računa maksimalnu visinu projektila
def max_height(v0, th):
    g = -9.81
    dt = 1e-5

    th = th*np.pi/180
    vy = v0*np.sin(th)

    y = 0.

    while vy>0:
        y += vy*dt
        vy += g*dt

    return float(y)

#funkcija koja računa domet projektila
def hor_range(v0, th):
    g = -9.81
    dt = 1e-5

    th = th*np.pi/180
    vx = v0*np.cos(th)
    vy = v0*np.sin(th)

    x = 0.
    y = 0.

    while y>=0:
        y += vy*dt
        vy += g*dt
        x += vx*dt

    return float(x)

#funkcija koja računa maksimualnu brzinu projektila
#unosi se i vrijeme putanje
#projektilu je dopušteno da padne ispod početne visine, inače bi maksimalna brzina uvijek bila jednaka početnoj
def max_speed(v0, th, t):
    g = -9.81
    dt = 1e-5

    th = th*np.pi/180
    vx = v0*np.cos(th)
    vy = v0*np.sin(th)

    vmax = v0

    N = int(t/dt)

    for i in range(N):
        vy += g*dt
        if vx*vx+vy*vy>vmax**2:
            vmax = np.sqrt(vx*vx+vy*vy)

    return float(vmax)

#gađanje mete
def target(v0, th, sx, sy, r):
    g = -9.81
    dt = 1e-5

    th = th*np.pi/180
    vx = v0*np.cos(th)
    vy = v0*np.sin(th)

    x = [0.]
    y = [0.]
    i = 0
    j = 0

    while y[i]>=0:
        d = np.sqrt((sx-x[i])**2+(sy-y[i])**2)-r

        if d<0:
            j = 1
            print ("Meta je pogođena.")
            break

        if i==0:
            dmin = d

        if d<dmin:
            dmin = d
            
        x += [x[i]+vx*dt]
        y += [y[i]+vy*dt]

        vy += g*dt
        i += 1

    if j==0:
        print("Meta nije pogođena. Najbliža postignuta udaljenost je {} metara".format(dmin))

    
    plt.plot(x,y, color="b")
    circle1 = plt.Circle((sx, sy), r, color="r")
    plt.gca().add_patch(circle1)
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.axis("equal")
    plt.show()