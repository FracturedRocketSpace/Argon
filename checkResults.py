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
@jit( nopython=True )
def ComputePressure(positions, temp, pressure, i):
    virial=0
    for p1 in range(config.nParticles):
        for p2 in range(config.nParticles):
            if p1 > p2:
                X = positions[p2,0] - positions[p1,0];
                Y = positions[p2,1] - positions[p1,1];
                Z = positions[p2,2] - positions[p1,2];
                
                X -= np.rint(X/config.lCalc) * config.lCalc;
                Y -= np.rint(Y/config.lCalc) * config.lCalc;
                Z -= np.rint(Z/config.lCalc) * config.lCalc;
                
                r2 = X*X + Y*Y + Z*Z;
                r2i = 1 / r2;
                r6i = r2i*r2i*r2i                
                force = 24  * r6i * (2*r6i - 1) * r2i;
                
                virial +=np. sqrt(r2) * -force
    #
    pressure[i] = config.kB * temp[i] - 1/(3*config.nParticles)*virial

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
def checkResults(particles, temp, eK, pressure, cV, i):
    ComputeeK(particles.velocities, eK, i)
    ComputeTemp(temp, eK, i)
    ComputePressure(particles.positions, temp, pressure, i)
    ComputeCv(particles.velocities, temp[i], eK[i], cV, i)
    
    