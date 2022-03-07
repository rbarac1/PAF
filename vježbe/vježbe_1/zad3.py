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


#nagib pravca
a = (y2-y1)/(x2-x1)

#pomak na y osi
b = y1 - a*x1

#printanje jednadbžbe pravca, za veću preciznost mijenjajte broj znamenki i decimala u ispisu floata
print("Jednažba pravca je y = {:5.4f} x + {:5.4f}".format(a,b))