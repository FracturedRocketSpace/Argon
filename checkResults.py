#

import config
import numpy as np
from numba import jit


#@jit( nopython=True )
def ComputeTemp(temp, eK, i):
    # Using Boltzmann equipartition theorem
    temp[i] = 2 * eK[i] / ( 3*(config.nParticles - 1) * config.kB)

#@jit( nopython=True )
def ComputeeK(velocities, eK, i):
    eK[i] = 0.5 * config.mass * np.sum(np.sum(velocities**2));
    
def checkResults(particles, temp, eK, i):
    ComputeeK(particles.velocities, eK, i)
    ComputeTemp(temp, eK, i)
    