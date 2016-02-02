# Move the argon particles

import numpy as np
import config as c
from calculateforces import calculateForces

def keepParticlesInCell(particles):
    for p in range(c.nParticles):
        particles.positions[p,:] = np.remainder(particles.positions[p,:], c.lCalc);

def argonMove(particles):
    for p1 in range(c.nParticles):
        particles.positions[p1,:] += particles.velocities[p1,:] * c.dt + 0.5 / c.mass*particles.forces[p1,:] * c.dt ** 2
        keepParticlesInCell(particles);
        particles.velocities[p1,:] += 0.5/c.mass*particles.forces[p1,:] * c.dt
        
    calculateForces(particles)
    for p1 in range(c.nParticles):
        particles.velocities[p1,:] += 0.5/c.mass*particles.forces[p1,:] * c.dt   


    
    
    

      


