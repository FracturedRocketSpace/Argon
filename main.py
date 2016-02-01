# Main file for argon

# Import classes and functions (In that order)
import config
from particles import Particles
from initSimulation import initSimulation
# Init function
# Atom update (Which itself includes pos+vel update / BC)
# Calculate temperature


# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);
# Main loop
for i in range(config.iterations):
    # Update position
    
    # Calculate temperature
    
    # Increment
    i=i;
    
# Plot temperature & positions

# Show program end
print("Program ended at i =", i);