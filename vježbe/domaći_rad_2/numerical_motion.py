def move(f, m, tmax, x0=0, v0=0, t0=0, dt=0.001):
    #početni uvjeti
    dt = tmax/1000.
    t = [t0]
    x = [x0]
    v = [v0]
    a = [f(v0, x0, t0)/m]

    #numeričko rješavanje
    while t[-1]<tmax:
        a += [f(v[-1], x[-1], t[-1])/m]
        v += [v[-1]+a[-1]*dt]
        x += [x[-1]+v[-1]*dt]
        t += [t[-1]+dt]

    return t,x,v,a