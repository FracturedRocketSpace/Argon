# Move the argon particles

import numpy as np
import config as c
from calculateforces import calculateForces

def keepParticlesInCell(particles):
    for p in range(c.nParticles):
        particles.positions[p,:] = np.remainder(particles.positions[p,:], c.lCalc);

def argonMove(particles):
    particles.positions += particles.velocities * c.dt + 0.5 / c.mass*particles.forces * c.dt ** 2
    #keepParticlesInCell(particles);
    particles.velocities += 0.5/c.mass*particles.forces* c.dt
        
    calculateForces(particles)
    particles.velocities += 0.5/c.mass*particles.forces * c.dt   


    
    
    

      


