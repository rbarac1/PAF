#include <iostream>

using namespace std;

int main(){
    //zadani koeficijenti
    float a1=5, b1=4, c1=1, a2=3, b2=-6, c2=2;

    //nepoznanice
    float x,y;

    //riješavanje sustava
    x = (c1-c2*b1/b2)/(a1-a2*b1/b2);
    y = (c1-a1*x)/b1;

    cout << "x = " << x << "\t y = " << y;
}