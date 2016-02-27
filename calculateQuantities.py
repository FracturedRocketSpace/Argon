# Calculate the various physical quantities during runtime

import config
import numpy as np

# Calculate the total kinetic energy
def computeEK(velocities, eK, i):
    eK[i] = 0.5 * np.sum(np.sum(velocities**2));

# Calculate temperature using the Boltzmann equipartition theorem
def computeTemp(temp, eK, i):
    temp[i] = 2 * eK[i] / ( 3*(config.nParticles - 1) )

# Calculate the Compressibility factor
def computeCompr(virial, temp, compr, i):
    compr[i] = 1 - virial /(3 * config.nParticles * temp[i]) 

# Calculate cV during runtime
def computeCV(velocities, eK, Cv, i):
    if( i > config.cVLength):
        eKmean = np.mean( eK[i-config.cVLength:i] );
        var = np.var( eK[i-config.cVLength:i] );
        Cv[i] =  3 * (eKmean**2) / (2*(eKmean**2) - 3*config.nParticles*(var)  )

# Calculate displacement
def computeDisplacement(positions, zeroPositions, displacement, i):
    if(i > config.stopRescaleIter):
        dR = (positions - zeroPositions);
        dR -= np.around(dR/config.lCalc)
        displacement[i] = 1/config.nParticles * np.sum( np.sum( (dR)**2, axis=1 ) )    

#
def calculateQuantities(particles, temp, eK, compr, virial, cV, displacement, zeroPositions, i):
    computeEK(particles.velocities, eK, i)
    computeTemp(temp, eK, i)
    computeCompr(virial, temp, compr, i)
    computeCV(particles.velocities, eK, cV, i)
    computeDisplacement(particles.positions, zeroPositions, displacement, i)
        
    # Set 0 displacement positions after rescale has ended
    if(i == config.stopRescaleIter):
        zeroPositions = np.copy(particles.positions);    