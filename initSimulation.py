# Init the atom particles

from initPositions import initPositions
from initVelocities import initVelocities
#import calculateForce

def initSimulation(particles):
    initPositions(particles);
    initVelocities(particles);
    #particles = calculateForce(particles);