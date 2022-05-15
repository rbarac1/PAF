#include "HarmonicOscillator.h"
#include <math.h>
#include <iostream>

using namespace std;

HarmonicOscillator::HarmonicOscillator(float x0, float v0, float k0, float m0){
    v = 1.*v0;
    x = 1.*x0;
    t = 0;
    a = -1.*k0/m0*x;
    k = k0; //moram kopirati k0 i m0 u nove varijable da se spreme za ostale funkcije
    m = m0;

    fx = fopen("x-t.dat", "w");
    fv = fopen("v-t.dat", "w");
    fa = fopen("a-t.dat", "w");
}

void HarmonicOscillator::evolve(){
    a = -1.*k/m*x;
    v += a*dt;
    x += v*dt;
    t += dt;
}

void HarmonicOscillator::oscillate(float T){
    for(int i=0; i*dt<=T; i++){
        fprintf(fx, "%f  %f\n", t, x);
        fprintf(fv, "%f  %f\n", t, v);
        fprintf(fa, "%f  %f\n", t, a);
        evolve();
    }
}


HarmonicOscillator::~HarmonicOscillator(){}