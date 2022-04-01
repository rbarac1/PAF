import numpy as np
import matplotlib.pyplot as plt

#unos varijabli je na dnu kodu, prije pozivanja funkcije kh

T = 10. #vrijeme gibanja u sekundama
g = -9.81 #akceleracija na površini Zemlje
N = 1e5 #broj intervala pri numeričkom riješavanju
dt = T/N #vremenska razlika između koraka

N = int(N)

#kosi hitac funkcija (računanje i plotanje)
def kh(v0, th):
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
    ax3.set_ylabel(r'$y[m]$')

    #plotanje
    plt.tight_layout()
    plt.show()


v_0 = 78. #početna brzina
theta = 48. #otklon od x osi u stupnjevima


kh(v_0,theta*np.pi/180)

