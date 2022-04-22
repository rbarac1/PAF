import numpy as np
import matplotlib.pyplot as plt
import projectile_drop as pd

###########################################
#   ZADATAK 1

p1 = pd.ProjectileDrop(2,200) #visina u km, brzina u m/s


(t, x, y) = p1.Tdrop(4.2, 500, 0)

print("Projektil se ispušta u trenutku t={}s".format(t))


(t, x, y) = p1.Tdrop(4.2, 500, 1)

print("Projektil se ispušta u trenutku t={}s".format(t))
