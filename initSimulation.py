# Init the atom particles

from initPositions import initPositions
from initVelocities import initVelocities
from calculateforces import calculateForces

def initSimulation(particles):
    initPositions(particles);
    initVelocities(particles);
    calculateForces(particles);