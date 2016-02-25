# Config file 

import numpy as np

animation = False;
animationIter = 10;
animationRotation = 0.50;

nParticles = 4 * (3**3); # = 4*n**3
iterations = 5000; # Number of iterations
epsilon = 1; # Strengt of potential energy in Joule 
sigma = 1 ; # 0 point of potential in meters
kB = 1; # Boltzmann constant in Joule per Kelvin
mass = 1; # Mass of argon in kg
tInitial = 0.8; # Initial temperature Kelvin
tRescale = tInitial; # Boundary temperature for solid walls in Kelvin
rescaleIter = 10;
stopRescaleIter = 1000;
oscLength=np.array([50, 100, 150, 200, 250, 300, 500]) #Length of wiggles in iterations; used for error calculation

cVLength=250; # Running average length for cV

rho=0.85; # Choose density in reduced units

dt = 0.004; # Time step (seconds)
lCalc =  (1/rho)**(1/3)*(nParticles/4)**(1/3)*2**(2/3);
a=np.sqrt(kB*tInitial/mass); # Used for Maxwell distribution

histRange = np.sqrt(2)*(lCalc)*3/5
histSteps = 150;
