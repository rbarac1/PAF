#include <stdio.h>

class HarmonicOscillator {
    private:

        float x0, v0, k, m, T, t, x, v, a, k0, m0;
        float dt=0.001;
        FILE *fx, *fv, *fa;
        
       void evolve();

    public:
        HarmonicOscillator(float x0, float v0, float k0, float m0);
        ~HarmonicOscillator();

        void oscillate(float T);

};