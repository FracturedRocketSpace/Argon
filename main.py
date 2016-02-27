# Main file for argon

# Import classes and functions
import config
import numpy as np
import timeit
from particles import Particles
from initSimulation import initSimulation
from argonMove import argonMove
from calculateQuantities import calculateQuantities
from particlesanimation import animationPlot
from postProcess import postProcess

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

postProcess(particles, temp, eK, eP, pressure, cV, displacement)

# Stop timer
stop = timeit.default_timer()
print("Program ended in  =", int(stop - start), "seconds");
print(round( ((stop - start)/config.iterations)*1000 , 3 ), "ms per iteration for", config.nParticles, "particles")