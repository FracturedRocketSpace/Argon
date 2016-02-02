#

import config
import scipy.spatial.distance as sc
from calculateforces import cellOffset


def ComputeTemp(particles, temp, eK, i):
    # Using Boltzmann equipartition theorem
    temp[i] = 2 * eK[i] / ( 3*(config.nParticles - 1) * config.kB)

def ComputeeK(particles, eK, i):
    eK[i] = 0.5 * config.mass * sum(sum(particles.velocities**2));
    
def ComputeeP(particles, eP, i):
    for p1 in range(0,config.nParticles):
        for p2 in range(0,p1):
            cell_offset = cellOffset( particles.positions[p1,:], particles.positions[p1,:] );
            new_p2_position = particles.positions[p2,:]+cell_offset*config.lCalc;
            r = sc.euclidean(particles.positions[p1,:],new_p2_position);
            V= 4*config.epsilon*((config.sigma/r)**12-(config.sigma/r)**6);
            eP[i] += V
    
def checkResults(particles, temp, eK, eP, i):
    ComputeeK(particles, eK, i)
    ComputeTemp(particles, temp,eK,  i)
    ComputeeP(particles, eP, i)
    