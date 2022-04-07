#include <iostream>

using namespace std;


//jednadžba pravca
void pravac(float x1, float y1, float x2, float y2){
    float a = (y2-y1)/(x2-x1);
    float b = y1 - a*x1;
    cout << "Jednadžba pravca je y=" <<a<<"x"<<"+"<<b;
}

int main(){
    //točke (x1, y1) i (x2, y2)
    float x1=4.,y1=-2.,x2=3.,y2=0.7;
    //pozivanje funkcije koja određuje jednadžbu pravca
    pravac(x1,y1,x2,y2);
}