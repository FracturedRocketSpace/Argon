# Config file 

import numpy as np

animation = False;
nParticles = 108;
iterations = 200; # Number of iterations
epsilon = 1; # Strengt of potential energy in Joule 
sigma = 1 ; # 0 point of potential in meters
kB = 1; # Boltzmann constant in Joule per Kelvin
mass = 1; # Mass of argon in kg
tInitial = 2.5; # Initial temperatyre Kelvin
tRescale = 2.5; # Boundary temperature for solid walls in Kelvin
rescaleIter = 25;

dt = 0.001; # Time step (seconds)
lCalc =  (nParticles/4)**(1/3)*2**(2/3);
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution
