import numpy as np

g = -9.81

class projectile:
    def __init__(self, v0, th, ro, Cd, A, m, x0=0, y0=0, dt=0.01):
        self.ro = ro
        self.Cd = Cd
        self.A = A
        self.m = m

        self.vx = [v0*np.cos(th*np.pi/180)]
        self.vy = [v0*np.sin(th*np.pi/180)]

        self.x = [x0]
        self.y = [y0]

        self.t = [0]
        self.dt = dt


    def __ac(self, vx, vy):
        return np.array([-1*np.sign(vx)*self.ro*self.Cd*self.A*vx*vx/2/self.m,g-np.sign(vy)*self.ro*self.Cd*self.A*vy*vy/2/self.m])


    def __move(self, met="RK4"):
        if met=="RK4":
            (k1vx, k1vy) = self.__ac(self.vx[-1], self.vy[-1])*self.dt
            (k1x, k1y) = (self.vx[-1]*self.dt, self.vy[-1]*self.dt)

            (k2vx, k2vy) = self.__ac(self.vx[-1]+k1vx/2, self.vy[-1]+k1vy/2)*self.dt
            (k2x, k2y) = ((self.vx[-1]+k1vx/2)*self.dt, (self.vy[-1]+k1vy/2)*self.dt)

            (k3vx, k3vy) = self.__ac(self.vx[-1]+k2vx/2, self.vy[-1]+k2vy/2)*self.dt
            (k3x, k3y) = ((self.vx[-1]+k2vx/2)*self.dt, (self.vy[-1]+k2vy/2)*self.dt)

            (k4vx, k4vy) = self.__ac(self.vx[-1]+k3vx, self.vy[-1]+k3vy)*self.dt
            (k4x, k4y) = ((self.vx[-1]+k3vx)*self.dt, (self.vy[-1]+k3vy)*self.dt)


            self.vx += [self.vx[-1]+ (k1vx+2*k2vx+2*k3vx+k4vx)/6]
            self.vy += [self.vy[-1]+ (k1vy+2*k2vy+2*k3vy+k4vy)/6]

            self.x += [self.x[-1]+ 1/6*(k1x+2*k2x+2*k3x+k4x)]
            self.y += [self.y[-1]+ 1/6*(k1y+2*k2y+2*k3y+k4y)]
            

        else:
            (ax, ay) = self.__ac(self.vx[-1], self.vy[-1])

            self.vx += [self.vx[-1]+ax*self.dt]
            self.vy += [self.vy[-1]+ay*self.dt]

            self.x += [self.x[-1]+self.vx[-1]*self.dt]
            self.y += [self.y[-1]+self.vy[-1]*self.dt]

        self.t += [self.t[-1]+self.dt]

    
    def reset(self):
        self.vx = [self.vx[0]]
        self.vy = [self.vy[0]]

        self.x = [self.x[0]]
        self.y = [self.y[0]]

        self.t = [0]


    def motion(self, method="RK4"):
        while self.y[-1]>=self.y[0]:
            self.__move(met=method)

        return self.x, self.y
        
    def range(self):
        self.reset()
        self.motion()

        return self.x[-1]