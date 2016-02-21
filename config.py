# Config file 

import numpy as np

animation = False;
animationIter = 10;
animationRotation = 0.50;

nParticles = 4 * (6**3); # = 4*n**3
iterations = 100; # Number of iterations
epsilon = 1; # Strengt of potential energy in Joule 
sigma = 1 ; # 0 point of potential in meters
kB = 1; # Boltzmann constant in Joule per Kelvin
mass = 1; # Mass of argon in kg
tInitial = 1; # Initial temperature Kelvin
tRescale = 1; # Boundary temperature for solid walls in Kelvin
rescaleIter = 20;
stopRescaleIter = 1000;
oscLength=np.array([50, 100, 150, 200, 250, 300, 500]) #Length of wiggles in iterations; used for error calculation

rho=0.65; # Choose density in reduced units

dt = 0.004; # Time step (seconds)
lCalc =  (1/rho)**(1/3)*(nParticles/4)**(1/3)*2**(2/3);
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution

histRange = np.sqrt(2*lCalc*lCalc) *3/4;
histSteps = 150;
