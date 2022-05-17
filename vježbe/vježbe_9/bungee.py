import numpy as np

#y predstavlja "dubinu" tj. prije skoka je y=0 te raste za vrijeme pada
g = 9.81 

class bungee:
    def __init__(self, ro, Cd, A, m, k, l, y0=0, dt=0.01):
        self.ro = ro
        self.Cd = Cd
        self.A = A
        self.m = m
        self.k = k
        self.l = l

        self.v = [0]

        self.y = [y0]

        self.t = [0]
        self.dt = dt


    def __ac(self, y, v):
        return g-np.sign(v)*self.ro*self.Cd*self.A*v*v/2/self.m-self.k*(y-self.l)*np.heaviside(y-self.l,0)/self.m


    def __move(self):
        k1v = self.__ac(self.y[-1], self.v[-1])*self.dt
        k1y = self.v[-1]*self.dt

        k2v = self.__ac(self.y[-1]+k1y/2, self.v[-1]+k1v/2)*self.dt
        k2y = (self.v[-1]+k1v/2)*self.dt

        k3v = self.__ac(self.y[-1]+k2y/2, self.v[-1]+k2v/2)*self.dt
        k3y = (self.v[-1]+k2v/2)*self.dt

        k4v = self.__ac(self.y[-1]+k3y, self.v[-1]+k3v)*self.dt
        k4y = (self.v[-1]+k3v)*self.dt

        self.v += [self.v[-1]+ (k1v+2*k2v+2*k3v+k4v)/6]

        self.y += [self.y[-1]+ 1/6*(k1y+2*k2y+2*k3y+k4y)]
            
        self.t += [self.t[-1]+self.dt]

    
    def reset(self):
        self.v = [self.v[0]]

        self.y = [self.y[0]]

        self.t = [0]

    def E_k(self):
        return 1./2*self.m*np.multiply(np.array(self.v), np.array(self.v))

    def E_g(self):
        return -self.m*g*np.array(self.y)

    def E_el(self):
        y_l = np.add(np.array(self.y),np.array(len(self.y)*[-1.*self.l]))
        return 1./2*self.k*np.heaviside(y_l,0)*np.multiply(y_l, y_l)

    def E_tot(self):
        return self.E_k()+self.E_g()+self.E_el()

    def jump(self, T=0):
        y_ex = 0.
        l_max= self.l
        if(self.ro*self.Cd*self.A==0):
            T = 10

        while (self.t[-1]<T if T!=0 else 1):
            self.__move()
            if(len(self.y)>100):
                y_old = self.y[-35]
                y_old2 = self.y[-100]
            if(self.v[-1]*self.v[-2]<0):
                if(y_ex==0.):
                    l_max = self.y[-1]
                if(np.abs(self.y[-1]-y_ex)<l_max/15):
                    break
                y_ex = self.y[-1]

        return self.t, self.y