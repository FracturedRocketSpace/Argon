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

def calcResult(pressure, eK, j):
    if(len(pressure)<config.stopRescaleIter+config.oscLength[j]):
        return 0,0,0,0;
        
    # Take pressure in stable region
    pressureStable=pressure[config.stopRescaleIter::]
    
    # Compute Average values
    pressureAvg=np.mean(pressureStable)
    cvAvg=ComputeCv(eK[config.stopRescaleIter::])

    # Ititiate averages for the sections
    pressureAvgSections=np.zeros(len(pressureStable)/config.oscLength[j]-1)
    cvAvgSections=np.zeros(len(eK)/config.oscLength[j]-1)

    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        pressureAvgSections[i]=np.mean(pressureStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        cvAvgSections[i]=ComputeCv(eK[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])

    # Compute error
    s2p=np.var(pressureAvgSections)
    pressureError=np.sqrt( s2p/len(pressureAvgSections) )    
    s2cv=np.var(cvAvgSections)
    cvError=np.sqrt( s2cv/len(cvAvgSections) )
    
    return pressureAvg, pressureError, cvAvg, cvError