# Main file for argon

# Import classes and functions
import config
import numpy as np
from particles import Particles
from initSimulation import initSimulation
from argonMove import argonMove
from plotResults import plotResults
import timeit
from particlesanimation import animationPlot
from calculateQuantities import calculateQuantities

# Start Timer
start = timeit.default_timer()

# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);

# Init check variables
temp = np.zeros(config.iterations);
eK = np.zeros(config.iterations);
eP = np.zeros(config.iterations);
compr = np.zeros(config.iterations);
cV = np.zeros(config.iterations);
displacement = np.zeros(config.iterations);
zeroPositions = np.zeros((config.nParticles,3));

if(config.animation):
    anim = animationPlot();

# Main loop
for i in range(config.iterations):
    # Update position
    virial = argonMove(particles, eP, temp, i);
    
    # Calculate physical quantities
    calculateQuantities(particles, temp, eK, compr, virial, cV, displacement, zeroPositions, i);
    
    # Update animation
    if(config.animation and i % config.animationIter == 0):
        anim.updateParticlePlot(particles);
    
    # Inform user of progress
    print("Iteration", i+1, "completed; Time is: ", round(i*config.dt, 3) );

# Calculate errors
for j in range( int( len(config.oscLength) ) ):
    print("Block length=",config.oscLength[j])              
    (pressureAvg, pressureError,cVAvg, cVError, tempAvg, tempError, ePParticleAvg, ePParticleError)=calcResult(pressure,eK,temp,eP,j)
    print("Compressibility factor=",pressureAvg,"; Error:",pressureError)
    print("cV=",cVAvg,"; Error:", cVError)
    print("Temperature=",tempAvg,"; Error:", tempError)
    print("Potential energy per particle=",ePParticleAvg,"; Error:",ePParticleError)
    print(" ")
    
# Convert Ek and Ep to per particle for use in plotting
eK /= config.nParticles;
eP /= config.nParticles;  

# Show program end
plotResults(particles, temp, eK, eP, pressure, cV, displacement)

# Stop timer
stop = timeit.default_timer()
print("Program ended in  =", int(stop - start), "seconds");
print(round( ((stop - start)/config.iterations)*1000 , 3 ), "ms per iteration for", config.nParticles, "particles")