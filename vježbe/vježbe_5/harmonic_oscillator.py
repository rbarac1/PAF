import numpy as np
import matplotlib.pyplot as plt


class HarmonicOscillator:
    def __init__(self):
        #prazne liste
        self.x = []
        self.v = []
        self.a = []
        self.t = []

    def init(self, m, k, x0, v0): #uvodi varijable i početne uvjete
        self.om = np.sqrt(k/m)

        self.x += [x0]
        self.v += [v0]
        self.a += [-k/m*x0]
        self.t += [0]

    def reset(self): #vraća na početne uvjete
        self.x = [self.x[0]]
        self.v = [self.v[0]]
        self.a = [self.a[0]]
        self.t = [0]


    def oscillate(self, t, dt=0.01): #oscilira t sekundi sa dt korakom
        #postavljanje granica i koraka
        N = int(t/dt)
        j = len(self.t)

        self.j = j-1
        self.N = N
        self.dt = dt

        for i in range(j, N+j): #osciliranje
            self.v += [self.v[i-1] + self.a[i-1]*dt]
            self.x += [self.x[i-1]+self.v[i]*dt]
            self.a += [-1*self.om**2*self.x[i]]
            self.t += [i*dt]

    def plot_trajectory(self, plot="show", t0=-1):
        if t0!=-1: #plotaj gibanje od zadanog t0
            self.j = int(t0/self.dt)

        if plot=="show": #pokaži graf numeričkih rješenja
            plt.figure(figsize=(12,6))

            for i in range(self.j, self.N): #plotanje samo num. rješenja
                plt.subplot(1,3,1)  #x-t
                plt.scatter(self.t[i], self.x[i], c="b", s= 8)
                plt.subplot(1,3,2)  #v-t
                plt.scatter(self.t[i], self.v[i], c="b", s= 8)
                plt.subplot(1,3,3)  #a-t
                plt.scatter(self.t[i], self.a[i], c="b", s= 8)

            plt.subplot(1,3,1)
            plt.title("x-t graf", fontsize=14)
            plt.xlabel("t[s]", fontsize=14)
            plt.ylabel("x[m]", fontsize=14)

            plt.subplot(1,3,2)
            plt.title("v-t graf", fontsize=14)
            plt.xlabel("t[s]", fontsize=14)
            plt.ylabel(r"v$\mathrm{\frac{m}{s}}$", fontsize=14)

            plt.subplot(1,3,3)
            plt.title("a-t graf", fontsize=14)
            plt.xlabel("t[s]", fontsize=14)
            plt.ylabel(r"a$\mathrm{\frac{m}{s^2}}$", fontsize=14)

            plt.tight_layout()
            plt.show()

        if t0==-1: #plotaj cijelo gibanje
            t = np.linspace(self.t[0], self.t[len(self.t)-1], 1e4)

            tnum = self.t
            xnum = self.x
            vnum = self.v
            anum = self.a

        else: #plotaj gibanje od t0
            t = np.linspace(self.t[self.j], self.t[len(self.t)-1], 1e4)

            tnum = []
            xnum =[]
            vnum = []
            anum = []

            for i in range(self.j, len(self.t)):
                tnum += [self.t[i]]
                xnum +=[self.x[i]]
                vnum += [self.v[i]]
                anum += [self.a[i]]


        A = np.sqrt(self.x[0]**2+(self.v[0]/self.om)**2)    #analitička amplituda
        fi = np.arctan(-self.v[0]/self.om/self.x[0])    #analitički fazni pomak

        xan = A*np.cos(self.om*t+fi)    #an. položaj
        van = -1*A*self.om*np.sin(self.om*t+fi) #an. brzina
        aan = -1*self.om**2*xan #an. akceleracija

        return tnum, xnum, vnum, anum, t, xan, van, aan

