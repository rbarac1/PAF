i=1
while i:
    try:
        x1,y1 = input('Unesite koordinate prve točke u formatu x,y: \t').split(',')
        float(x1)
        float(y1)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0


i=1
while i:
    try:
        x2,y2 = input('Unesite koordinate druge točke u formatu x,y: \t').split(',')
        float(x2)
        float(y2)
    except ValueError:
        print("Ponovite upis")
    except:
        print("Ponovite upis")
    else:
        i = 0
