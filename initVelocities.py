"""
Compute intitial velocities

"""


import numpy as np
import config
import scipy.stats as stats



def initVelocities(particles):             
    # Speeds
    speed=stats.maxwell.rvs(loc=0,scale=config.a,size=config.nParticles)          
    
    # Vectors       
    phi = np.random.uniform(0, np.pi*2, config.nParticles)
    costheta = np.random.uniform(-1, 1, config.nParticles)
    theta = np.arccos( costheta )
    particles.velocities[:,0] = speed * np.sin( theta ) * np.cos( phi )
    particles.velocities[:,1] = speed * np.sin( theta ) * np.sin( phi )
    particles.velocities[:,2] = speed * np.cos( theta )
        
    # Set center of mass velocity to zero
    particles.velocities -= np.mean(particles.velocities,axis=0);