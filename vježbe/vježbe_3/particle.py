import numpy as np
import matplotlib.pyplot as plt

g = -9.81

class Particle:
    def __init__(self):
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []

    def set_initial_conditions(self, v_0, th, x_0, y_0, dt):
        self.th = th*np.pi/180
        self.v_0 = v_0
        self.dt = dt

        self.vx += [v_0*np.cos(self.th)]
        self.vy += [v_0*np.sin(self.th)]
        self.x += [x_0]
        self.y += [y_0]

    def reset(self):
        self.__init__()

    def __move(self):
        self.vx += [self.vx[len(self.vx)-1]]
        self.vy += [self.vy[len(self.vy)-1]+g*self.dt]
        self.x += [self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
        self.y += [self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]

    def range(self):
        while(self.y[len(self.y)-1]>=self.y[0]):
            self.__move()
        return(self.x[len(self.x)-1])
    
    def plot_trajectory(self):
        if(len(self.x)==1): #u slučaju da se nije pozvao move
            plt.scatter(self.x[0], self.y[0])
            plt.xlabel("x[m]")
            plt.ylabel("y[m]")
            plt.show()
            return 0

        plt.plot(self.x, self.y)
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()


    def printInfo(self):
        print("Cestica ima masu {0:.2f} i u pocetnome trenutku nalazi se na polozaju x={1:.2f}".format(self.mass, self.x_0))