#include <iostream>

using namespace std;


//funkcija
int kr(float sx, float sy, float r, float x, float y){
    if ((x-sx)*(x-sx)+(y-sy)*(y-sy)<r*r)
        return 1;
    else
        return 0;
}

int main(){
    //koordinate središta kružnice, radijus kružnice i koordinate točke
    float sx=1, sy=1, r=2, x=0, y=0;

    //pozivanje funkcije
    if (kr(sx,sy,r,x,y))
        cout << "Točka se nalazi unutar kružnice.";
    else
        cout << "Točka se ne nalazi unutar kružnice.";
}