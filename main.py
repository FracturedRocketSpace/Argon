# Main file for argon

# Import classes and functions
import config
import numpy as np
from particles import Particles
from initSimulation import initSimulation
from argonMove import argonMove
from checkResults import checkResults
from plotResults import plotResults
import timeit
from particlesanimation import animationPlot
from rescaleVelocity import rescaleVelocity
import matplotlib.pyplot as plt

# Start Timer
start = timeit.default_timer()

# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);

# Init check variables
temp = np.zeros(config.iterations);
eK = np.zeros(config.iterations);
eP = np.zeros(config.iterations);

if(config.animation):
    anim = animationPlot();

# Main loop
for i in range(config.iterations):
    # Update position
    argonMove(particles);
    # Calculate temperature
    checkResults(particles, temp, eK, eP, i);
    # Rescale 
    if (i+1) % config.rescaleIter == 0:
        rescaleVelocity(particles, temp[i])
    #
    print("Iteration", i+1, "completed; Time is: ", round(i*config.dt, 3) );
    
    if(config.animation):
        anim.updateParticlePlot(particles);

# Show program end
plotResults(particles, temp, eK, eP)

# Stop timer
stop = timeit.default_timer()
print("Program ended in  =", int(stop - start), "seconds");