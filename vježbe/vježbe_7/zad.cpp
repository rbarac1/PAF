#include <iostream>
#include "Particle.h"

using namespace std;

int main(){
    Particle p1(100,45,0,0);
    cout << "Domet čestice 1 je: ";
    p1.range();
    cout << "Vrijeme leta čestice 1 je: ";
    p1.time();

    Particle p2(10,60,0,0);
    cout << "Domet čestice 2 je: ";
    p2.range();
    cout << "Vrijeme leta čestice 2 je: ";
    p2.time();


    return 0;
}