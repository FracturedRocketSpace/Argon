# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:54:44 2016

@author: Mathijs
"""
import config
import numpy as np

def calcResult(pressure, cV, temp, j):
    if(len(pressure)<config.stopRescaleIter+config.oscLength[j]):
        return 0,0,0,0;
        
    # Take pressure in stable region
    pressureStable=pressure[config.stopRescaleIter::]
    cVStable=cV[config.stopRescaleIter::]
    tempStable=temp[config.stopRescaleIter::]
    
    # Compute Average values
    pressureAvg=np.mean(pressureStable)
    cVAvg=np.mean(cVStable)
    tempAvg=np.mean(tempStable)

    # Ititiate averages 
    AvgPressure=np.zeros(len(pressureStable)/config.oscLength[j]-1)
    AvgCV=np.zeros(len(cVStable)/config.oscLength[j]-1)
    AvgTemp=np.zeros(len(tempStable)/config.oscLength[j]-1)

    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        AvgPressure[i]=np.mean(pressureStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        AvgCV[i]=np.mean(cVStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        AvgTemp[i]=np.mean(tempStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])

    # Compute error
    s2p=np.var(AvgPressure)
    pressureError=np.sqrt( s2p/len(AvgPressure) )    
    s2cv=np.var(AvgCV)
    cVError=np.sqrt( s2cv/len(AvgCV) )
    s2temp=np.var(AvgTemp)
    tempError=np.sqrt(s2temp/len(AvgTemp))
    
    return pressureAvg, pressureError, cVAvg, cVError, tempAvg, tempError