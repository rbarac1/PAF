import numpy as np
import matplotlib.pyplot as plt


#funkcija
def kr(xt,yt,xs,ys,r):

    #provjera položaja točke u odnsou na kružnicu
    if (xs-xt)**2+(ys-yt)**2>r**2:
        print("Točka se nalazi izvan kružnice.")
    elif (xs-xt)**2+(ys-yt)**2<r**2:
        print("Točka se nalazi unutar kružnice.")
    else:
        print("Točka se nalazi na kružnici.")

    #crtanje točke i kružnice
    plt.scatter(xt,yt, color='red')
    circle1 = plt.Circle((xs,ys), r, color='blue', fill=False)
    plt.gca().add_patch(circle1)
    plt.axis('equal')
    
    #ako nas zanima udaljenost od središta kružnice, onda na kraju idućeg reda ne oduzimamo r
    print("Točka se nalazi 2na položaju ({},{}) i udaljena je za {} od kružnice.".format(xt,yt,np.abs(np.sqrt((xs-xt)**2+(ys-yt)**2)-r)))
    
    #izbor ispisa grafa
    g = int(input("Ako želite ispisati graf na ekranu upišite 1, a ako želite spremiti graf u pdf upišite 2: "))

    if g==1:
        plt.show()
    elif g==2:
        ime = input("Unesite ime datoteke:")
        print("Graf je spremljen u file pod imenom "+ime+".pdf")
        plt.savefig(ime+".pdf")
    
    return 0



#funkcija je dovršena i sada možemo provjeriti je li radi
#podatke možemo unijeti kroz terminal(tj. user input) kao u 3. zadatku 

#unos i provjera koordinata točke
i=1
while i:
    try:
        xt,yt = input('Unesite koordinate točke u formatu x,y: \t').split(',')
        xt = float(xt)
        yt = float(yt)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0


#unos i provjera koordinata središta kružnice
i=1
while i:
    try:
        xs,ys = input('Unesite koordinate središta kružnice u formatu x,y: \t').split(',')
        xs = float(xs)
        ys = float(ys)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0

#unos i provjera radijusa kružnice
i=1
while i:
    try:
        r = float(input('Unesite radijus kružnice: \t'))
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0


#pozivanje funkcije
kr(xt,yt,xs,ys,r)
