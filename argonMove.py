# Move the argon particles

import numpy as np
import config as c
from calculateforces import calculateForces
from numba import jit

@jit( nopython=True )
def keepParticlesInCell(positions):
    for p in range(c.nParticles):
        positions[p,:] = np.remainder(positions[p,:], c.lCalc);

def argonMove(particles, eP, i):
    particles.positions += particles.velocities * c.dt + 0.5 / c.mass*particles.forces * c.dt ** 2
    keepParticlesInCell(particles.positions);
    particles.velocities += 0.5/c.mass*particles.forces* c.dt
        
    particles.forces = calculateForces(particles.positions, particles.forces, eP, i)
    particles.velocities += 0.5/c.mass*particles.forces * c.dt   


    
    
    

      


