#derivacija u točki
def met1(f, x, dx, met=3): #(funkcija, točka u kojoj se derivira, širina intervala, metoda)
    if met==2:
        return (f(x+dx)-f(x))/dx

    else:
        return (f(x+dx)-f(x-dx))/dx/2

#derivacija u intervalu a-b
def met2(f, a, b, dx, met=3): #(funkcija, granice interavala a i b, dx, metoda)
    x = []
    derx = []

    for i in range(int((b-a)/dx)+1):
        x += [a+i*dx]
        derx += [met1(f, x[i], dx, met)]

    return x, derx


#pravokutna integracija, vraća gornju i donju među
def pint(f, a, b, N):
    dx = (b-a)/float(N)
    s1 = 0. #gornja međa
    s2 = 0. #donja međa

    for i in range(N):
        s1 += f(a+(i+1)*dx)
        s2 += f(a+i*dx)

    return s1*dx, s2*dx

#trapezna integracija
def tint(f, a, b, N):
    dx = (b-a)/float(N)
    s = (f(a)+f(b))/2

    for i in range(1, N):
        s += f(a+i*dx)
    
    return s*dx

