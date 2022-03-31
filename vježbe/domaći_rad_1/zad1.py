import particle as prt
import numpy as np

p1 = prt.Particle()
p1.set_initial_conditions(10, 60, 0, 0) #(v0, kut u stupnjevima, x0, y0, dt=0.001)

t_total = p1.total_time()
print("Ukupno vrijeme gibanja je {:.4} s".format(t_total))

t = 1.8
p1.set_initial_conditions(10, 60, 0, 0) #potrebno za resetiranje gibanja
max_v = p1.max_speed(t)
print("Maksimalna brzina za vrijeme gibanja od {:.4} s je {:.4} m/s".format(float(t), max_v))


th = 31
(v1, v2) = p1.velocity_to_hit_target(th, 10, 4, 2) #(kut, x središta kuglice, y središta kuglice, radijus kuglice)

if v2>-1: #ako je moguće pogoditi
    print("Brzina za pogoditi metu pod kutem od {} stupnjeva treba biti veća od {}, a manja od {}.".format(th,round(v2,2), round(v1,2) if round(v1-0.01,2)>-0.01 else "beskonačno"))



v = 13
(th1, th2) = p1.angle_to_hit_target(v, 10,4,2) #(zadana brzina, koordinate kuglice, radijus kuglice)
if th1!=400: #ako je moguće pogoditi
    print("Projektil početne brzine {} može pogoditi kuglicu ako je ispaljen pod kutevima {} ili {}.".format(round(v,2),round(th1,2),round(th2,2)))
