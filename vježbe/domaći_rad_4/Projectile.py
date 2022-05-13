import numpy as np

g = -9.81

class projectile:
    def __init__(self, v0, ro, Cd, m, ar, shape="no", th=45, x0=0, y0=0, dt=0.01):
        self.ro = ro
        self.Cd = Cd
        self.m = m
        self.th = th
        self.v0 = v0

        self.vx = [v0*np.cos(self.th*np.pi/180)]
        self.vy = [v0*np.sin(self.th*np.pi/180)]

        self.x = [x0]
        self.y = [y0]

        self.t = [0]
        self.dt = dt

        if shape=="cube":
            self.a = ar
        
        if shape=="sphere":
            self.A = np.pi*ar*ar

        if shape=="no":
            self.A = ar

        self.shape = shape


    def __ac(self, vx, vy):
        return np.array([-1*np.sign(vx)*self.ro*self.Cd*self.A*vx*vx/2/self.m,g-np.sign(vy)*self.ro*self.Cd*self.A*vy*vy/2/self.m])

    def __Acube(self): #dvije plohe su uvijek paralelne s tlom, a vektor brzine je uvijek u ravnini paralelnoj iste dvije plohe od preostale 4
        #oba načina ispod daju isti rezultat
        #self.A = self.a*self.a*np.abs(np.cos(np.arctan(np.abs(self.vy[-1]/self.vx[-1]))-np.pi/4))*np.sqrt(2)
        self.A = np.dot(self.a*self.a*np.array([1,1]), np.abs(np.array([self.vx[-1], self.vy[-1]]))/np.sqrt(self.vx[-1]**2+self.vy[-1]**2))

    def __move(self, met="RK4"):
        if self.shape=="cube":
            self.__Acube()

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
        self.vx = [self.v0*np.cos(self.th*np.pi/180)]
        self.vy = [self.v0*np.sin(self.th*np.pi/180)]

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

    def set_target(self, xm, ym, rm):
        #prebacit ću metu desno od točke ispaljivanja projektila
        #ako je meta bila lijevo, onda je potreban kut ispaljivanja 
        if(xm<self.x[0]):
            self.corr = -1
            self.xm = -1*xm
        else:
            self.corr = 1
            self.xm = xm
            
        self.ym = ym
        self.rm = rm

    def __hit_angle(self):
        if(self.corr==-1):
            return 180-self.th
        else:
            return self.th

    def __distance_to_target(self): #jednostavnije je uzeti kvadrat udaljenosti
        return (self.xm-self.x[-1])**2+(self.ym-self.y[-1])**2

    def __move_to_target(self):
        d_old = self.__distance_to_target()
        self.__move()
        d_new = self.__distance_to_target()

        while((d_new < d_old) or self.vy[-1]>0):
            d_old = d_new
            self.__move()
            d_new = self.__distance_to_target()

            if d_old<self.rm*self.rm:
                break

        return d_old

    def hit_target(self):
        i = 1
        while(self.__move_to_target()>self.rm*self.rm):
            i += 1
            if(i>100):
                return 500, self.x, self.y

            if((self.vy[-1]>0 and self.y[-1]<self.ym) or (self.vy[-1]<0 and self.x[-1]>self.xm)):
                self.th = (3*self.th*90)/4

            elif(self.vy[-1]<0 and self.x[-1]<self.xm):
                self.th *= 0.9

            self.reset()

        return self.__hit_angle(), self.corr*np.array(self.x), self.y

        
