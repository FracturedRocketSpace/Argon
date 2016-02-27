#Post processing of simulation

import config
import numpy as np
from plotResults import plotResults

def postProcess(particles, temp, eK, eP, compr, cV, displacement):
    
    (comprStable, tempStable,ePStableParticle,eKStable) = computeStable(compr,eK,temp,eP)  
    (comprAvg, cVAvg,tempAvg,ePParticleAvg) = computeAverages(comprStable,tempStable,ePStableParticle,eKStable)
    
    # Calculate and display errors for multiple block sizes
    for j in range( len(config.oscLength) ):
        print("Block length=",config.oscLength[j])              
        (comprError,cVError, tempError, ePParticleError)=computeErrors(comprStable,eKStable,tempStable,ePStableParticle,j)
        displayQuantities(comprAvg, comprError,cVAvg, cVError, tempAvg, tempError, ePParticleAvg, ePParticleError)
        
    # Plot the results
    
    #calculate Ek and Ep to per particle for use in plotting
    eKPerParticle = eK / config.nParticles;
    ePPerParticle = eP / config.nParticles;  
    
    plotResults(particles, temp, eKPerParticle, ePPerParticle, compr, cV, displacement)

def computeCv(eK):
    eKmean = np.mean(eK);
    eKvar = np.var(eK);
    
    return 3 * (eKmean**2) / (2*(eKmean**2) - 3*config.nParticles*(eKvar)  )

def computeStable(compr,eK,temp,eP):

    # Take pressure in stable region
    comprStable=compr[config.stopRescaleIter::]
    tempStable=temp[config.stopRescaleIter::]
    ePStable=eP[config.stopRescaleIter::]
    ePStableParticle=ePStable/config.nParticles
    eKStable=eK[config.stopRescaleIter::]    
    
    return comprStable, tempStable, ePStableParticle, eKStable

def computeAverages(comprStable,tempStable,ePStableParticle,eKStable):
    # Compute Average values
    comprAvg=np.mean(comprStable)
    cVAvg=computeCv(eKStable)
    tempAvg=np.mean(tempStable)
    ePParticleAvg=np.mean(ePStableParticle)
    
    return comprAvg, cVAvg,tempAvg,ePParticleAvg
    
def displayQuantities(comprAvg, comprError,cVAvg, cVError, tempAvg, tempError, ePParticleAvg, ePParticleError):
    print("Compressibility factor=",comprAvg,"; Error:",comprError)
    print("cV=",cVAvg,"; Error:", cVError)
    print("Temperature=",tempAvg,"; Error:", tempError)
    print("Potential energy per particle=",ePParticleAvg,"; Error:",ePParticleError)
    print(" ")
    
def computeErrors(comprStable,eKStable,tempStable,ePStableParticle,j):

    if(len(comprStable)<config.oscLength[j]):
        return 0,0,0,0;

    # Ititiate averages 
    comprAvgSections=np.zeros(len(comprStable)/config.oscLength[j])
    cVAvgSections=np.zeros(len(eKStable)/config.oscLength[j])
    tempAvgSections=np.zeros(len(tempStable)/config.oscLength[j])
    ePParticleAvgSections=np.zeros(len(ePStableParticle)/config.oscLength[j])

    # Loop over all sections, calculate avg of parameters in sections
    for i in range( int( (config.iterations-config.stopRescaleIter) / config.oscLength[j] -1 ) ):
        comprAvgSections[i]=np.mean(comprStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]])
        cVAvgSections[i]=computeCv(eKStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]])
        tempAvgSections[i]=np.mean(tempStable[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]])
        ePParticleAvgSections[i]=np.mean(ePStableParticle[i*config.oscLength[j]:i*config.oscLength[j]+config.oscLength[j]])

    # Compute error
    s2p=np.var(comprAvgSections)
    comprError=np.sqrt( s2p/len(comprAvgSections) )    
    s2cv=np.var(cVAvgSections)
    cVError=np.sqrt( s2cv/len(cVAvgSections) )
    s2temp=np.var(tempAvgSections)
    tempError=np.sqrt(s2temp/len(tempAvgSections))
    s2ePParticle=np.var(ePParticleAvgSections)
    ePParticleError=np.sqrt(s2ePParticle/len(ePParticleAvgSections))    
    
    return comprError,cVError, tempError, ePParticleError
    