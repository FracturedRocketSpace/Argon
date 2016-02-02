#

import config
import numpy as np
import scipy.spatial.distance as sc
from calculateforces import cellOffset



def ComputeTemp(particles, temp, eK, i):
    # Using Boltzmann equipartition theorem
    temp[i] = 2 * eK[i] / ( 3*(config.nParticles - 1) * config.kB)

def ComputeeK(particles, eK, i):
    eK[i] = 0.5 * config.mass * sum(sum(particles.velocities**2));
    
def ComputeeP(particles, eP, i):
    for p1 in range(0,config.nParticles):
        #for p2 in range(p1):
        cell_offset = cellOffset(particles.positions[p1,:], particles.positions[range(p1),:]) ;
        new_p2_position = particles.positions[range(p1),:] + cell_offset*config.lCalc;
        r =  np.sum( (particles.positions[p1,:]-new_p2_position)**2, axis=1) #actually r^2
        
        V = 4 * config.epsilon * ((config.sigma/r)**6-(config.sigma/r)**3)        
        eP[i] += sum(V)
    
def checkResults(particles, temp, eK, eP, i):
    ComputeeK(particles, eK, i)
    ComputeTemp(particles, temp,eK,  i)
    ComputeeP(particles, eP, i)
    