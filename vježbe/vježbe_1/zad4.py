#funkcija za jednadžbu pravca
def pr(x1, y1, x2, y2):
    #nagib pravca
    a = (y2-y1)/(x2-x1)
    #pomak na y osi
    b = y1 - a*x1
    #jednadžba pravca
    print("y = {:5.4f} x + {:5.4f}".format(a,b))
    return a,b


#pozivanje funkcije
pr(1,2,2,3)