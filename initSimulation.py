# Init the simulation by placing the argon in a FCC grid and initalizing the velocities according to the maxwell distribution
# Afterwards we also initialize the forces

from calculateforces import calculateForces
import numpy as np
import scipy.stats as stats
import config

def initPositions(positions):
    # Number and length of FCC unit cells    
    # The number of unit cells has to be large enough so that all particles can be placed
    Nc = 0;
    while 4*(Nc ** 3) < config.nParticles:
        Nc += 1;
    Lcell = config.lCalc/Nc;
    
    # Positions of particles in FCC unit cell
    # The +0.25 is to prevent placing the particles on boundary
    xCell = np.array([0, 0.5, 0.5, 0]) + 0.25;
    yCell = np.array([0, 0.5, 0, 0.5]) + 0.25;
    zCell = np.array([0, 0, 0.5, 0.5]) + 0.25;
    
    # Generate position array
    n=0; # Used to count number of placed particles
    for x in range(Nc):
        for y in range(Nc):
            for z in range(Nc):
                for k in range(4):
                    if n<config.nParticles:
                        positions[n,0] = (x + xCell[k] ) * Lcell
                        positions[n,1] = (y + yCell[k] ) * Lcell
                        positions[n,2] = (z + zCell[k] ) * Lcell
                        n += 1
                        
def initVelocities(velocities):             
    # Generate total velocity
    speed = stats.maxwell.rvs(loc=0,scale=config.a,size=config.nParticles)          
    
    # Generate a random direction  
    phi = np.random.uniform(0, np.pi*2, config.nParticles)
    costheta = np.random.uniform(-1, 1, config.nParticles)
    theta = np.arccos( costheta )
    
    # Initalize the velocity vectors    
    velocities[:,0] = speed * np.sin( theta ) * np.cos( phi )
    velocities[:,1] = speed * np.sin( theta ) * np.sin( phi )
    velocities[:,2] = speed * np.cos( theta )
        
    # Set center of mass velocity to zero
    velocities -= np.mean(velocities,axis=0);

def initSimulation(particles):
    initPositions(particles.positions);
    initVelocities(particles.velocities);
    particles.forces,virial = calculateForces(particles.positions, particles.forces, np.array([0,0]), 0);