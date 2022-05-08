#include "Particle.h"
#include <math.h>
#include <iostream>

using namespace std;

Particle::Particle(double v0, double th, double x0, double y0){
    t=0;
    dt=0.001;
    g=-9.81;

    vx=v0*cos(th/180*M_PI);
    vy=v0*sin(th/180*M_PI);
    x=x0;
    y=y0;

}

void Particle::evolve(){
    t+=dt;
    vx += 0.;
    vy += g*dt;
    x += vx*dt;
    y += vy*dt;

}

double Particle::range(){
    while(y >= 0)
        evolve();
    
    cout << x << "m." << endl;
    return x-x0;
}



double Particle::time(){
    while(y >= 0)
        evolve();
    cout << t << "s." << endl;
    return t;
}

Particle::~Particle(){}