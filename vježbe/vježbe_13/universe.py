#koristit ću mjerne jedinice gdje je masa izražena preko mase zemlje, udaljenost u AU, a vrijeme u godinama

import numpy as np

#G u novim jedinicama
G = 6.674e-11*5.9742e24/1.496e11/1.496e11/1.496e11*3.154e7*3.154e7

class Cobject:
    def __init__(self, m, x0, y0, vx, vy):
        self.m = m
        self.v = np.array([vx, vy])
        self.r = np.array([[x0, y0]])

    
class Universe:
    def __init__(self):
        self.objects = []
        self.t = [0]
        
    def addobject(self, Cobject):
        self.objects += [Cobject]

    def __move(self):
        for current in self.objects:
            a = np.array([0., 0.])
            for other in self.objects:
                if current != other:
                    dr = current.r[-1,:]-other.r[-1,:]
                    a += -G*other.m*dr/(np.dot(dr,dr)**1.5)

            current.v = current.v+a*self.dt
            current.r = np.append(current.r, [current.r[-1]+current.v*self.dt], 0)

        self.t += [self.t[-1]+self.dt]

    def evolve(self,T,dt=0.001):
        self.dt = dt
        current_T = self.t[-1]
        while self.t[-1]-current_T<T:
            self.__move()

    def reverse(self):  #time reversal
        N = len(self.t)
        for i in range(int(N/2)):
            for object in self.objects:
                temp = object.r[i,0]
                object.r[i,0] = object.r[N-i-1,0]
                object.r[N-i-1,0] = temp

                temp = object.r[i,1]
                object.r[i,1] = object.r[N-i-1,1]
                object.r[N-i-1,1] = temp