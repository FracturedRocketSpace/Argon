# Config file 

import numpy as np

nParticles = 32;
iterations = 200; # Number of iterations
epsilon = 1; # Strengt of potential energy in Joule 
sigma = 1 ; # 0 point of potential in meters
kB = 1; # Boltzmann constant in Joule per Kelvin
mass = 1; # Mass of argon in kg
tInitial = 10; # Initial temperatyre Kelvin
tRescale = 300; # Boundary temperature for solid walls in Kelvin
rescaleIter = 50;

dt = 0.001; # Time step (seconds)
lCalc =  2; #(nParticles/4)**(1/3) * sigma * (2** (2/3) );
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution
