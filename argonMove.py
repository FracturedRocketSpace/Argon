# Move the argon particles
import numpy as np
import config
from numba import jit

# Rescale velocity to get wanted temperature
def rescaleVelocity(velocities, temp):
    velocities *= np.sqrt(config.tRescale/temp)

# Place particles back on the other side of the cell if they left it
def keepParticlesInCell(positions):
        positions = np.remainder(positions, config.lCalc);
        
# Calculate the forces. Jitted to make is super fast
# Code has been based on: http://combichem.blogspot.nl/2013/04/fun-with-numba-numpy-and-f2py.html
@jit( nopython=True )
def calculateForces(positions, forces, eP, i):
    # Reset variables
    forces=np.zeros(shape=(config.nParticles,3))
    virial = 0;
    
    for p1 in range(config.nParticles):
        for p2 in range(config.nParticles):
            if p1 > p2:
                # Calculate seperation and find nearest image
                X = positions[p2,0] - positions[p1,0];
                Y = positions[p2,1] - positions[p1,1];
                Z = positions[p2,2] - positions[p1,2];
                X -= np.rint(X/config.lCalc) * config.lCalc;
                Y -= np.rint(Y/config.lCalc) * config.lCalc;
                Z -= np.rint(Z/config.lCalc) * config.lCalc;
                
                # Calculate the total force, potential energy and virial
                r2 = X*X + Y*Y + Z*Z;
                r2i = 1 / r2;
                r6i = r2i*r2i*r2i
                
                force = 24  * r6i * (2*r6i - 1) * r2i;
                eP[i] += 4 * r6i * (r6i - 1);
                virial -= r2 * force;
                
                # Apply forces on particles
                forces[p1,0] -= force * X;
                forces[p1,1] -= force * Y;
                forces[p1,2] -= force * Z;
                
                forces[p2,0] += force * X; 
                forces[p2,1] += force * Y; 
                forces[p2,2] += force * Z; 
    return forces, virial

def argonMove(particles, eP, temp, i):   
    # Rescale velocities
    if ( (i+1) % config.rescaleIter == 0 and i < config.stopRescaleIter ):
        rescaleVelocity(particles.velocities, temp[i-1])
        
    # Velocity Verlet Algorithm
    particles.positions += particles.velocities * config.dt + 0.5 / particles.forces * config.dt ** 2
    keepParticlesInCell(particles.positions);
    particles.velocities += 0.5/particles.forces* config.dt
        
    particles.forces, virial = calculateForces(particles.positions, particles.forces, eP, i)
    particles.velocities += 0.5/particles.forces * config.dt   

    return virial