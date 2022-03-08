import numpy as np
import matplotlib.pyplot as plt


#modificirana funkcija iz 4. zadatka
#funkcija za jednadžbu pravca
def pr(x1, y1, x2, y2):
    #nagib pravca
    a = (y2-y1)/(x2-x1)
    #pomak na y osi
    b = y1 - a*x1
    #jednadžba pravca
    print("y = {:5.4f} x + {:5.4f}".format(a,b))

    #izbor ispisa grafa
    g = int(input("Ako želite ispisati graf na ekranu upišite 1, a ako želite spremiti graf u pdf upišite 2: "))
    
    x = np.arange(min(x1, x2)-2, max(x1,x2)+2)
    y = a*x+b
    plt.plot(x, y)
    plt.scatter([x1,x2],[y1,y2], c='r')

    if g==1:
        plt.show()
    elif g==2:
        print("Graf je spremljen u file pod imenom pravac.pdf")
        plt.savefig("pravac.pdf")
    return a,b,g


#dio koda iz 3. zadatka
#unos i provjera koordinata prve točke
i=1
while i:
    try:
        x1,y1 = input('Unesite koordinate prve točke u formatu x,y: \t').split(',')
        x1 = float(x1)
        y1 = float(y1)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0


#unos i provjera koordinata druge točke
i=1
while i:
    try:
        x2,y2 = input('Unesite koordinate druge točke u formatu x,y: \t').split(',')
        x2 = float(x2)
        y2 = float(y2)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0


pr(x1, y1, x2, y2)