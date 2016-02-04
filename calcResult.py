# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:54:44 2016

@author: Mathijs
"""
import config
import numpy as np

def calcResult(pressure, cV):
    # Take pressure in stable region
    pressureStable=pressure[config.stopRescaleIter::]
    cVStable=cV[config.stopRescaleIter::]
    
    # Compute Average values
    pressureAvg=np.mean(pressureStable)
    cVAvg=np.mean(cVStable)

    # Ititiate averages 
    AvgPressure=np.zeros(len(pressureStable)/config.oscLength-1)
    AvgCV=np.zeros(len(cVStable)/config.oscLength-1)

    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength -1 ) ):
        AvgPressure[i]=np.mean(pressureStable[i*config.oscLength:i*config.oscLength+config.oscLength-1])
        AvgCV[i]=np.mean(cVStable[i*config.oscLength:i*config.oscLength+config.oscLength-1])

    # Compute error
    s2p=np.var(AvgPressure)
    pressureError=np.sqrt( s2p/len(AvgPressure) )    
    s2cv=np.var(AvgCV)
    cVError=np.sqrt( s2cv/len(AvgCV) )
    
    
    
    return pressureAvg, pressureError, cVAvg, cVError