import numpy as np


class qp:
    def __init__(self, q, m, v0, E, B, f, dt=0.01):
        self.m = m
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)

        self.v = np.array([v0])

        self.r = np.array([[0,0,0]])

        self.t = [0]
        self.dt = dt

        self.f = f

    def new_function(self,f):
        self.f = f

    def __ac(self, v):
        return self.q*(self.E+np.cross(v, self.B))/self.m

    def __move(self, met="RK4"):
        if(self.f(1)!=1):
            self.B[2] = self.f(self.t[-1])
        if met=="RK4":
            k1v = self.__ac(self.v[-1])*self.dt
            k1r = self.v[-1]*self.dt

            k2v = self.__ac(self.v[-1]+k1v/2)*self.dt
            k2r = (self.v[-1]+k1v/2)*self.dt

            k3v = self.__ac(self.v[-1]+k2v/2)*self.dt
            k3r = (self.v[-1]+k2v/2)*self.dt

            k4v = self.__ac(self.v[-1]+k3v)*self.dt
            k4r = (self.v[-1]+k3v)*self.dt

            self.v = np.append(self.v, [self.v[-1]+ (k1v+2*k2v+2*k3v+k4v)/6], 0)

            self.r = np.append(self.r, [self.r[-1]+ 1/6*(k1r+2*k2r+2*k3r+k4r)], 0)
                
            self.t += [self.t[-1]+self.dt]
        
        else:
            #print(self.v)
            a = self.__ac(self.v[-1])
            self.v = np.append(self.v, [self.v[-1]+a*self.dt],0)
            self.r = np.append(self.r, [self.r[-1]+self.v[-1]*self.dt],0)
            self.t += [self.t[-1]+self.dt]


    def reset(self):
        self.v = np.array([self.v[0]])
        self.r = np.array([self.r[0]])
        self.t = [0]


    def motion(self, T, method="RK4"):
        while(self.t[-1]<T):
            #print(self.r)
            self.__move(method)

        return self.r
