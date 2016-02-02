# calculateForce

import numpy as np
import config as c
#import scipy.spatial.distance as sc

#calculate cell offset
def cellOffset(current, other):
    return np.around((current-other)/c.lCalc);

#calculate forces
def calculateForces(particles):
    particles.forces=np.zeros(shape=(c.nParticles,3), dtype="float64")
    for p1 in range(1,c.nParticles):
        #for p2 in range(p1):
        cell_offset = cellOffset(particles.positions[p1,:], particles.positions[range(p1),:]) ;
        new_p2_position = particles.positions[range(p1),:] + cell_offset*c.lCalc;
        r =  np.sum( (particles.positions[p1,:]-new_p2_position)**2, axis=1) 
        force = np.multiply(24 * c.epsilon / c.sigma * (particles.positions[p1,:]-new_p2_position), 
                            (2*(c.sigma/r)**7-(c.sigma/r)**4)[np.newaxis].T)
        particles.forces[p1,:] += sum(force);
        particles.forces[range(p1),:] += -force;