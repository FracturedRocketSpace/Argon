# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:54:44 2016

@author: Mathijs
"""
import config
import numpy as np

def ComputeCv(eK):
    eKmean = np.mean(eK);
    eKvar = np.var(eK);
    
    return 3 * (eKmean**2) / (2*(eKmean**2) - 3*config.nParticles*(eKvar)  )
    
def errorBootstrap(data, numSamples):
    #initialize samples to zero
    samples=np.zeros(numSamples)
    pointsPerSample = np.floor(len(data)/2)
    for i in range(numSamples):
        samples[i] = np.mean(np.random.choice(data,pointsPerSample,False));
        
    s2 = np.var(samples);
    return np.sqrt(s2/len(data))

def calcResult(pressure, eK, temp, eP, j):
    # Take pressure in stable region
    pressureStable = pressure[config.stopRescaleIter::]
    eKStable = eK[config.stopRescaleIter::]
    ePStable = eP[config.stopRescaleIter::]
    tempStable = temp[config.stopRescaleIter::]
    
    # Compute Average values
    pressureAvg=np.mean(pressureStable)
    cVAvg=ComputeCv(eKStable)
    ePAvg=np.mean(ePStable)
    tempAvg=np.mean(tempStable)
    
    # Ititiate averages 
    avgPressureSections=np.zeros(len(pressureStable)/config.oscLength[j]-1)
    avgCvSections=np.zeros(len(eKStable)/config.oscLength[j]-1)
    avgePSections=np.zeros(len(eKStable)/config.oscLength[j]-1)
    avgTempSections=np.zeros(len(tempStable)/config.oscLength[j]-1)
    
    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        avgPressureSections[i]=np.mean(pressureStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        avgCvSections[i]=ComputeCv(eKStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        avgePSections[i]=np.mean(ePStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        avgTempSections[i]=np.mean(tempStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
    
    pressureError = errorBootstrap(avgPressureSections,10);
    cVError = errorBootstrap(avgCvSections,10);
    ePError = errorBootstrap(avgePSections,10);
    tempError = errorBootstrap(avgTempSections,10);
        
    return pressureAvg, pressureError, cVAvg, cVError, tempAvg, tempError, ePAvg, ePError