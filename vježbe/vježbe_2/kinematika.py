import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(T, F, m, x0, v0):
    #T,F,m - vrijeme gibanja u sekundama, sila u Newtonima, masa u kg
    #x0, v0 - početni položaj u metrima, brzina u m/s

    v = [v0] #početna brzina
    x = [x0] #početni položaj

    T = 1.0*T
    a = 1.0*F/m #akceleracija

    N = 1e5 #broj koraka pri numeričkom riješavanju

    dt = T/N #vremenska razlika između koraka

    N = int(N)

    #numeričko računanje brzine i položaja
    for i in range(N):
        v += [v[i]+a*dt]
        x += [x[i]+v[i+1]*dt]

    t = np.linspace(0, T, N+1)

    fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(12,6))

    #graf položaja
    ax1.plot(t,x, c='b')
    ax1.title.set_text('Položaj')
    ax1.set_xlabel(r'$t[s]$')
    ax1.set_ylabel(r'$x[m]$')

    #graf brzine
    ax2.plot(t,v, c='r')
    ax2.title.set_text('Brzina')
    ax2.set_xlabel(r'$t[s]$')
    ax2.set_ylabel(r'$v[m/s]$')

    #graf akceleracije
    ax3.plot(t,len(t)*[a], c='g')
    ax3.title.set_text('Akceleracija')
    ax3.set_xlabel(r'$t[s]$')
    ax3.set_ylabel(r'$a[m/s^2]$')

    #plotanje
    plt.tight_layout()
    plt.show()




#kosi hitac funkcija (računanje i plotanje)
def kosi_hitac(T, v0, th):
    #T - vrijeme gibanja u sekundama
    th *= np.pi/180
    T = 1.0*T
    g = -9.81 #akceleracija na površini Zemlje
    N = 1e5 #broj intervala pri numeričkom riješavanju
    dt = T/N #vremenska razlika između koraka

    N = int(N)

    x = [0.] #početni položaj - x komponenta
    y = [0.] #početni položaj - y komponenta
    vx = [1.0*v0*np.cos(th)] #početna brzina - x komponenta
    vy = [1.0*v0*np.sin(th)] #početna brzina - y komponenta

    #numeričko računanje brzine i položaja
    for i in range(N):
        vx += [vx[0]]
        vy += [vy[i]+g*dt]

        x += [x[i]+vx[i+1]*dt]
        y += [y[i]+vy[i+1]*dt]
    
    t = np.linspace(0, T, N+1)

    fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(12,6))

    #crtanje grafova
    #graf položaja
    ax1.plot(x,y, c='b')
    ax1.title.set_text('putanja čestice (x-y graf)')
    ax1.axis('equal')
    ax1.set_xlabel(r'$x[m]$')
    ax1.set_ylabel(r'$y[m]$')

    #graf brzine
    ax2.plot(t,x, c='r')
    ax2.title.set_text('x položaj u vremenu (x-t graf)')
    ax2.set_xlabel(r'$t[s]$')
    ax2.set_ylabel(r'$x[m]$')

    #graf akceleracije
    ax3.plot(t,y, c='g')
    ax3.title.set_text('y položaj u vremenu (y-t graf)')
    ax3.set_xlabel(r'$t[s]$')
    ax3.set_ylabel(r'$ym]$')

    #plotanje
    plt.tight_layout()
    plt.show()