#include <iostream>
#include "HarmonicOscillator.h"

using namespace std;

int main(){
    HarmonicOscillator h1(1,0,1,1); //(x0, v0, k, m)
    h1.oscillate(20);

    return 0;
}