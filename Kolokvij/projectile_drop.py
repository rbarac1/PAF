import numpy as np
import matplotlib.pyplot as plt

g = -9.81

class ProjectileDrop:
    def __init__(self, h, vx):  #visina u km, brzina u m/s
        self.vx0 = vx
        self.h = 1000*h

        self.vx = [vx]
        self.vy = [0]
        self.x = [0]
        self.y = [self.h]
        self.t = [0]

        print("Stvoren je avion sa početnom brzinom brzinom {}m/s na visini {}km.".format(vx, h))

    def set_height(self, h):    #promjena visine
        self.y = [1000*h]
        self.vx = [self.vx[-1]]
        self.vy = [self.vy[-1]]
        self.x = [self.x[-1]]
        self.t = [self.t[-1]]

        print("Visina je promijenjena na {}km.".format(h))

    def add_hvelocity(self, dvx):   #promjena horizontalne brzine
        self.y = [self.y[-1]]
        self.vx = [self.vx[-1]+dvx]
        self.vy = [self.vy[-1]]
        self.x = [self.x[-1]]
        self.t = [self.t[-1]]

        print("Horizontalna brzina je promijenjena za {}m/s. Novi iznos je {}m/s.".format(dvx, self.vx[-1]))

    def drop(self, dt=0.01):    #dt u sekundama
        while(self.y[-1]>0):
            self.vx += [self.vx[-1]]
            self.vy += [self.vy[-1]+g*dt]
            self.x += [self.x[-1]+self.vx[-1]*dt]
            self.y += [self.y[-1]+self.vy[-1]*dt]
            self.t += [self.t[-1]+dt]

        return dt, self.t, self.x, self.y, self.vy


    def reset(self):
        self.vx = [self.vx[0]]
        self.vy = [0]
        self.x = [0]
        self.y = [self.y[0]]
        self.t = [0]


    def num_T(self, dtnum):
        self.reset()

        return self.drop(dt=dtnum)[1][-1]

    def Tdrop(self, xtarget, wtarget, wind_v): #položaj mete u km, širina mete u m, brzina vjetra u m/s
        xtarget *= 1000 #km u m
        self.reset()
        self.vx = [self.vx[0]+wind_v] #neki čudan vjetar
        self.drop()
        T_old = self.t[-1]
        T_change = 0.5    #promjena vremena u sekundama

        while(np.abs(self.x[-1]-xtarget)>wtarget):
            if(self.x[-1]<xtarget):
                i = 1

            else:
                i = -1

            T_old = self.t[-1]
            x_old = self.x[-1]
            self.reset()
            self.vx = [self.vx[0]+wind_v]
            self.t = [T_old+i*T_change]
            self.drop()

        plt.plot(self.x, self.y)
        plt.show()

        return self.t[0], self.x, self.y



