#

import config
import numpy as np

#@jit( nopython=True )
def ComputeTemp(temp, eK, i):
    # Using Boltzmann equipartition theorem
    temp[i] = 2 * eK[i] / ( 3*(config.nParticles - 1) * config.kB)

#@jit( nopython=True )
def ComputeeK(velocities, eK, i):
    eK[i] = 0.5 * config.mass * np.sum(np.sum(velocities**2));

# Calculate beta*P/rho instead of just pressure
# Check if 6 or 3!
#@jit( nopython=True )
def ComputePressure(virial, temp, pressure, i):
    pressure[i] = 1 - virial /(6*config.nParticles *config.kB * temp[i])

#
#@jit( nopython=True )
def ComputeE2mean(velocities):
    return np.sum((0.5 * config.mass * np.sum(velocities**2, axis=1))**2);

#
#@jit( nopython=True )
def ComputeCv(velocities, eK, Cv, i):
    e2K = ComputeE2mean(velocities);
    
    Cv[i] = 1/( 2/(3*config.nParticles) - (e2K - eK**2)/(eK**2) );
    
    
def ComputeDisplacement(positions, zeroPositions, displacement, i):
    dR = (positions - zeroPositions);
    
    dR[:,0] -= np.around(dR[:,0]/config.lCalc)
    dR[:,1] -= np.around(dR[:,1]/config.lCalc)
    dR[:,2] -= np.around(dR[:,2]/config.lCalc)
    
    displacement[i] = 1/config.nParticles * np.sum( np.sum( (dR)**2, axis=1 ) )    

#    
def checkResults(particles, temp, eK, pressure, virial, cV, displacement, zeroPositions, i):
    ComputeeK(particles.velocities, eK, i)
    ComputeTemp(temp, eK, i)
    ComputePressure(virial, temp, pressure, i)
    ComputeCv(particles.velocities, eK[i], cV, i)
    if(i > config.stopRescaleIter):
        ComputeDisplacement(particles.positions, zeroPositions, displacement, i)
    
    