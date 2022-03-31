import numpy as np
import matplotlib.pyplot as plt

g = -9.81

class Particle:
    def __init__(self):
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []
        self.t = []

    def set_initial_conditions(self, v_0, th, x_0, y_0, dt=0.001):
        self.reset()
        self.th = th*np.pi/180
        self.v_0 = v_0
        self.x_0 = x_0
        self.y_0 = y_0
        self.dt = dt

        self.vx += [v_0*np.cos(self.th)]
        self.vy += [v_0*np.sin(self.th)]
        self.x += [x_0]
        self.y += [y_0]
        self.t += [0.]

    def reset(self):
        self.__init__()

    def __move(self):
        self.vx += [self.vx[len(self.vx)-1]]
        self.vy += [self.vy[len(self.vy)-1]+g*self.dt]
        self.x += [self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
        self.y += [self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]
        self.t += [len(self.t)*self.dt]



    #NOVA FUNKCIJA
    #############################################
    #############################################
    #pomiče projektil do točke neometane putanje koja je najbliža središtu mete
    def __move_to_target(self):
        self.dmin = np.sqrt((self.sx-self.x_0)**2+(self.sy-self.y_0)**2)
        self.__move()
        d2_old = (self.x[0]-self.sx)**2+(self.y[0]-self.sy)**2
        d2_new = (self.x[1]-self.sx)**2+(self.y[1]-self.sy)**2
        while d2_new<d2_old: #kada se udaljenost od mete krene povećavati putanja se zaustavi
            self.dmin = np.sqrt(d2_new)
            d2_old = d2_new
            self.__move()
            d2_new = (self.x[len(self.x)-1]-self.sx)**2+(self.y[len(self.y)-1]-self.sy)**2


    def range(self):
        while(self.y[len(self.y)-1]>=self.y[0]):
            self.__move()
        return self.x[len(self.x)-1]
    
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




    #NOVE FUNKCIJE IZ ZADAĆE
    ##########################
    ##########################
    def total_time(self):
        while(self.y[len(self.y)-1]>=self.y[0]):
            self.__move()
        return self.t[len(self.t)-1]


    def max_speed(self, time):
        vmax = float(self.v_0)
        N = int(time/self.dt)

        for i in range(N):
            self.__move()
            if self.vx[i]*self.vx[i]+self.vy[i]*self.vy[i]>vmax*vmax:
                vmax = np.sqrt(self.vx[i]*self.vx[i]+self.vy[i]*self.vy[i])

        return vmax


    #nepotrebno komplicirano... računa cijele intervale mogućih brzina za pogoditi metu
    def velocity_to_hit_target(self, th,  sx, sy, r, x_0=0., y_0=0.):
        v = 2.
        self.dmin = np.sqrt((sx-x_0)**2+(sy-y_0)**2) #min. udaljenost od središta mete (zasad)
        self.sx = sx
        self.sy = sy
        self.r = r
        delta_t = 0.1

        if self.dmin<=r:
            print("Meta je pogođena za sve iznose brzine.")
            return -2, -2
    
        while self.dmin>r: #dok god je projektil izvan mete
            dmin_old = self.dmin
            self.set_initial_conditions(v, th, x_0, y_0, dt=delta_t)
            self.__move_to_target() #pomičemo projektil do točke u putanji koja je najbliža meti

            #u slučaju pogotka, vraćamo se korak unazad, poboljšamo aproksimaciju i pokušamo ponovo
            #ovo se izvršava puno brže nego da smo odmah krenili sa jako malim dt
            if self.dmin<r and delta_t>1e-4:
                self.dmin = dmin_old
                delta_t *= 0.1
                continue

            if self.dmin<r:
                break

            i = len(self.y)-1
            #provjera je li dt premali
            if i>10:
                #ako je brzina manja od potrebne povećavamo je za neki faktor
                if (self.y[i]-self.y[i-1]<0 and np.abs(self.x[i])<np.abs(sx)) or (self.y[i]-self.y[i-1]>0 and self.y[i]<sy):
                    v *= 3

                else:#ako je brzina manja od potrebne povećavamo je za neki (različit) faktor
                    v *= 0.5
                #ovakav algoritam puno brže traži rješenje nego algoritam kojim stalno dodajemo (zbrajamo) isti broj


            else:
                if delta_t>1e-4:
                    delta_t *= 0.1
                
                else:
                    print("Nemoguće je pogoditi metu iz ovog kuta.")
                    return -1, -1
            
            if v>1e6:
                print("Nemoguće je pogoditi metu iz ovog kuta.")
                return -1, -1

        #ako je meta uspješno pogođena, sada tražimo min i max brzinu za pogodak
        v1 = v
        v2 = v
        dv = v/10

        dt0 = self.t[len(self.t)-1]/100
        delta_t = dt0

        self.dmin = 0
        i=1
        
        while self.dmin<=r: #traženje minimalne brzine
            if v1==v:
                self.set_initial_conditions(1e5, th, x_0, y_0, dt=dt0*v*1e-5)
                self.__move_to_target()
                if self.dmin<r:
                    v1 = -1+dv+0.01
                    break
                self.dmin = 0

            self.set_initial_conditions(v1, th, x_0, y_0, dt=delta_t)
            self.__move_to_target()

            if v1>1e5: #u slučaju da nema gornje granice
                v1 = -1+dv+0.01
                break

            if self.dmin>r and (dv>1e-3 or dv>v2/10000 or i==0): #pogodak i korekcija
                v1 -= dv
                self.dmin = 0
                
                if i==1:
                    dv *= 0.1
                
                if (dv<1e-2 or dv>v2/1000) and delta_t>dt0/10:
                    delta_t *= 0.1

                i=0
                continue

            if v1>100*v+dv: #povećavamo korak traženja u slučaju da je gornja granica puno veća od početnog pogotka
                v1*=100
                dv=v1/100

            i=1
            v1 += dv
            
        v1-=dv        


        dv = v/10
        delta_t = dt0
        i = 1
        self.dmin = 0

        while self.dmin<=r: #gotovo sve isto samo tražimo donju granicu
            self.set_initial_conditions(v2, th, x_0, y_0, dt=delta_t)
            self.__move_to_target()

            if self.dmin>r and (dv>1e-3 or dv>v2/10000 or i==0):
                v2 += dv
                self.dmin = 0
                
                if i==1:
                    dv *= 0.1

                if (dv<1e-2 or dv<v2/1000) and delta_t>dt0/10:
                    delta_t *= 0.1
                
                i=0
                continue

            if v2<1e-2:
                v2 = 0-dv
                break

            i=1
            v2 -= dv
            

        v2+=dv
        return v1, v2



    ###########
    def angle_to_hit_target(self, v,  sx, sy, r, x_0=0., y_0=0.):
        k = 1
        if sx<x_0: #provjera sa koje strane se nalazi meta
            k = -1

        th1 = np.arctan(sy/sx)*180/np.pi #projektil ne može dobiti kinetičku energiju
        th2 = 90.

        self.dmin = np.sqrt((sx-x_0)**2+(sy-y_0)**2)
        self.sx = sx
        self.sy = sy
        self.r = r

        delta_t = 0.01
        dth = 1.*k
        i = 1

        if k==-1:
            th1 = 180-th1


        if self.dmin<=r:
            print("Meta je pogođena za sve brzine.")
            return 400, 0
        
        while self.dmin>r: #slično kao traženje brzine u prethodnoj funkciji
            self.set_initial_conditions(v, th1, x_0, y_0, dt=delta_t)
            self.__move_to_target()

            if len(self.y)>10:
                if self.dmin<r and (np.abs(dth)>1e-2 or i==0):
                    th1 -= dth
                    self.dmin = r+1
                
                    if i==1:
                        dth *= 0.1

                    if dth<1e-1 and delta_t>1e-3:
                        delta_t *= 0.1
                    
                    i=0
                    continue

            else:
                delta_t *= 0.1

            i = 1
            th1 += dth

            if np.abs(th1)>360:
                print("Metu je nemoguće pogoditi.")
                return 400, 0

        th1 -= dth

        #radimo korekciju ako je moguća, sigurnije je ne gađati rub mete
        self.set_initial_conditions(v, th1+50*dth, x_0, y_0, dt=delta_t)
        self.__move_to_target()
        if  self.dmin<r:
            th1 += 50*dth


        self.dmin = r+1
        dth = k*1.
        delta_t = 0.01
        i = 1
    
        while self.dmin>r:
            self.set_initial_conditions(v, th2, x_0, y_0, dt=delta_t)
            self.__move_to_target()


            if len(self.y)>10:
                if self.dmin<r and (np.abs(dth)>1e-2 or i==0):
                    th2 += dth
                    self.dmin = r+1
                
                    if i==1:
                        dth *= 0.1

                    if dth<1e-1 and delta_t>1e-3:
                        delta_t *= 0.1
                    
                    i=0
                    continue

            else:
                delta_t *= 0.1

            i = 1
            th2 -= dth

        th2 += dth

        #udaljavanje od ruba
        self.set_initial_conditions(v, th1-50*dth, x_0, y_0, dt=delta_t)
        self.__move_to_target()
        if  self.dmin<r:
            th1 -= 50*dth 
        
        return th1, th2

        

    def printInfo(self):
        print("Cestica ima masu {0:.2f} i u pocetnome trenutku nalazi se na polozaju x={1:.2f}".format(self.mass, self.x_0))