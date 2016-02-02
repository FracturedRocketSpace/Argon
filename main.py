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

# Start Timer
start = timeit.default_timer()

# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);

# Init check variables
temp = np.zeros(config.iterations);
eK = np.zeros(config.iterations);
eP = np.zeros(config.iterations);

# Main loop
for i in range(config.iterations):
    # Update position
    print(particles.positions[1,:])
    print(particles.velocities[1,:])
    argonMove(particles);
    print(particles.positions[1,:])
    print(particles.velocities[1,:])
    # Calculate temperature
    checkResults(particles, temp, eK, eP, i);
    #
    print("Iteration =", i);
    

# Show program end
plotResults(temp, eK, eP)

# Stop timer
stop = timeit.default_timer()
print("Program ended in  =", int(stop - start), "seconds");