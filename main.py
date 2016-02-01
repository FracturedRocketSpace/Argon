# Main file for argon

# Import classes and functions (In that order)
import config
import numpy as np
import matplotlib.pyplot as plt
from particles import Particles
from initSimulation import initSimulation
from ComputeTemp import ComputeTemp
# Init function
# Atom update (Which itself includes pos+vel update / BC)
# Calculate temperature


# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);
# Main loop
Temp=np.zeros(config.iterations)
for i in range(config.iterations):
    # Update position
    
    # Calculate temperature
    Temp[i]=ComputeTemp(particles)
    
# Plot temperature & positions

# Show program end
print("Program ended at i =", i);
plt.plot(Temp)