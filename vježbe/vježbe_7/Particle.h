class Particle {
    private:

        double t, x, y, vx, vy, x0, y0;
        double dt=0.001;
        double g=-9.81;
        
       void evolve();

    public:
        Particle(double v0, double th, double x0, double y0);
        ~Particle();

        double range();
        double time();

};