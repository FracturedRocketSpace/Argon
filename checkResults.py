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

#
#@jit( nopython=True )
def ComputePressure(virial, temp, pressure, i):
    pressure[i] = config.kB * temp[i] - (virial * config.nParticles/(config.lCalc**3) )/(3*config.nParticles) 

#
#@jit( nopython=True )
def ComputeE2mean(velocities):
    return np.sum((0.5 * config.mass * np.sum(velocities**2, axis=1))**2)/config.nParticles;

#
#@jit( nopython=True )
def ComputeCv(velocities, temp, eK, Cv, i):
    
    Emean = eK / config.nParticles; 
    E2mean = ComputeE2mean(velocities);
    
    Cv[i] = (E2mean - Emean**2)/(config.kB*temp**2);

#    
def checkResults(particles, temp, eK, pressure, virial, cV, i):
    ComputeeK(particles.velocities, eK, i)
    ComputeTemp(temp, eK, i)
    ComputePressure(virial, temp, pressure, i)
    ComputeCv(particles.velocities, temp[i], eK[i], cV, i)
    
    