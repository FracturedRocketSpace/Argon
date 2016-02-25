
import config
import numpy as np

def ComputeCv(eK):
    eKmean = np.mean(eK);
    eKvar = np.var(eK);
    
    return 3 * (eKmean**2) / (2*(eKmean**2) - 3*config.nParticles*(eKvar)  )

def calcResult(pressure, eK, temp, eP, j):

    if(len(pressure)<config.stopRescaleIter+config.oscLength[j]):
        return 0,0,0,0;
        
    # Take pressure in stable region
    pressureStable=pressure[config.stopRescaleIter::]
    tempStable=temp[config.stopRescaleIter::]
    ePStable=eP[config.stopRescaleIter::]
    ePStableParticle=ePStable/config.nParticles
    
    # Compute Average values
    pressureAvg=np.mean(pressureStable)
    cVAvg=ComputeCv(eK[config.stopRescaleIter::])
    tempAvg=np.mean(tempStable)
    ePParticleAvg=np.mean(ePStableParticle)

    # Ititiate averages 
    AvgPressure=np.zeros(len(pressureStable)/config.oscLength[j]-1)
    cvAvgSections=np.zeros(len(eK)/config.oscLength[j]-1)
    #AvgCV=np.zeros(len(cVStable)/config.oscLength[j]-1)
    AvgTemp=np.zeros(len(tempStable)/config.oscLength[j]-1)
    AvgePParticle=np.zeros(len(ePStableParticle)/config.oscLength[j]-1)

    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        AvgPressure[i]=np.mean(pressureStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        cvAvgSections[i]=ComputeCv(eKStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        AvgTemp[i]=np.mean(tempStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])
        AvgePParticle[i]=np.mean(ePStableParticle[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]-1])

    # Compute error
    s2p=np.var(AvgPressure)
    pressureError=np.sqrt( s2p/len(AvgPressure) )    
    s2cv=np.var(cvAvgSections)
    cVError=np.sqrt( s2cv/len(cvAvgSections) )
    s2temp=np.var(AvgTemp)
    tempError=np.sqrt(s2temp/len(AvgTemp))
    s2ePParticle=np.var(AvgePParticle)
    ePParticleError=np.sqrt(s2ePParticle/len(AvgePParticle))    
    
    return pressureAvg, pressureError, cVAvg, cVError, tempAvg, tempError, ePParticleAvg, ePParticleError
    