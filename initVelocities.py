"""
Compute intitial velocities

"""


import numpy as np
import config
import scipy.stats as stats



def initVelocities(particles):             
    for i in range(config.nParticles):  
        # Speeds
        speed=stats.maxwell.rvs(loc=0,scale=config.a,size=1)          
        
        # Vectors       
        phi = np.random.uniform(0,np.pi*2)
        costheta = np.random.uniform(-1,1)
        theta = np.arccos( costheta )
        particles.velocities[i,0] = speed * np.sin( theta ) * np.cos( phi )
        particles.velocities[i,1] = speed * np.sin( theta ) * np.sin( phi )
        particles.velocities[i,2] = speed * np.cos( theta )
        
    return particles
