# Config file 

import numpy as np

animation = False;
nParticles = 4 * (4**3); # = 4*n**3
iterations = 3000; # Number of iterations
epsilon = 1; # Strengt of potential energy in Joule 
sigma = 1 ; # 0 point of potential in meters
kB = 1; # Boltzmann constant in Joule per Kelvin
mass = 1; # Mass of argon in kg
tInitial = 1; # Initial temperatyre Kelvin
tRescale = 1; # Boundary temperature for solid walls in Kelvin
rescaleIter = 50;
stopRescaleIter = 1000;

dt = 0.005; # Time step (seconds)
lCalc =  (nParticles/4)**(1/3)*2**(2/3);
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution
