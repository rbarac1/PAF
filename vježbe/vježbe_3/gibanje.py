import particle as prt
import numpy as np

dt = 0.1

p1 = prt.Particle()
p1.set_initial_conditions(10, 60, 0, 0, dt) #(v0, kut u stupnjevima, x0, y0, dt)

#numeričko rješenje
num_sol = p1.range()

p1.plot_trajectory()

#analitičko rješenje
an_sol = p1.v_0**2/9.81*np.sin(2*p1.th)

#funkcija za error
def err(num, an):
    return 100*np.abs((num-an)/an)

error = err(num_sol, an_sol)

print("Numeričko rješenje je {}, a analitičko je {}. Greška je {}%".format(num_sol, an_sol, error))
