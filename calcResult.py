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

def errorBootstrap(sections, numSamples, function):
    #initialize samples to zero
    samples=np.zeros(numSamples)
    sectionsPerSample = np.floor(len(sections)/2)
    for i in range(numSamples):
        samples[i] = function(sections[np.random.choice(sections.shape[0], sectionsPerSample, replace=False),:].flatten());
        
    s2 = np.var(samples);
    return np.sqrt(s2/len(sections))

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
    pressureSections=np.zeros((len(pressureStable)/config.oscLength[j]-1, config.oscLength[j]-1))
    cvSections=np.zeros((len(eKStable)/config.oscLength[j]-1, config.oscLength[j]-1))
    ePSections=np.zeros((len(ePStable)/config.oscLength[j]-1, config.oscLength[j]-1))
    tempSections=np.zeros((len(tempStable)/config.oscLength[j]-1, config.oscLength[j]-1))
    
    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        pressureSections[i]=pressureStable[i*config.oscLength[j]:(i+1)*config.oscLength[j]-1]
        cvSections[i]=eKStable[i*config.oscLength[j]:(i+1)*config.oscLength[j]-1]
        ePSections[i]=ePStable[i*config.oscLength[j]:(i+1)*config.oscLength[j]-1]
        tempSections[i]=tempStable[i*config.oscLength[j]:(i+1)*config.oscLength[j]-1]
    
    pressureError = errorBootstrap(pressureSections,50, np.mean);
    cVError = errorBootstrap(cvSections,50, ComputeCv);
    ePError = errorBootstrap(ePSections,50, np.mean);
    tempError = errorBootstrap(tempSections,50, np.mean);
        
    return pressureAvg, pressureError, cVAvg, cVError, tempAvg, tempError, ePAvg, ePError