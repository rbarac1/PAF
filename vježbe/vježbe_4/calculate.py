import modul
import math

def f1(x):
    return x*x-2*x

def f2(x):
    return math.sin(x)

print(modul.value(f1,1))
print(modul.value(f2,1))