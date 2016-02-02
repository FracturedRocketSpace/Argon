# Config file

import numpy as np

nParticles = 108;
iterations = 10; # Number of iterations
dt = (10 ** (-12)); # Time step (seconds)
epsilon = 1.65 * (10 ** (-21)); # Strengt of potential energy in Joule 
sigma = 3.4 * (10 ** (-10)) ; # 0 point of potential in meters
kB = 1.38 * (10 ** (-23)); # Boltzmann constant in Joule per Kelvin
mass = 6.69 * (10 ** (-26)); # Mass of argon in kg
tInitial = 300; # Initial temperatyre Kelvin
tBoundary = 300; # Boundary temperature for solid walls in Kelvin
lCalc = int( (nParticles/4)**(1/3) ) * 525.6 * (10 ** (-26)); # Length of calculation cell in meters, 525.6 pm is unitCell
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution
