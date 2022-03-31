import kosihitac as kh

#prva varijabla je svugdje početna brzina
#druga varijabla je svugdje početni kut gibanja u odnosu na horizontalu

kh.khplot(10, 60) #plotanje putanje

h = kh.max_height(10, 60) #max visina
d = kh.hor_range(10, 60) #domet
v = kh.max_speed(10, 60, 2) #max brzina, 3. varijabla je vrijeme gibanja

print("Maksimalna visina projektila je {:.4} m, domet je {:.4} m, a maksimalna brzina je {:.4} m/s".format(h,d,v))

#plotanje gađanja mete
#zadnje 3 varijable su po redu: x koordinata središta mete, y koordinata središta mete, radijus mete
kh.target(13, 73.74, 10, 4, 2)