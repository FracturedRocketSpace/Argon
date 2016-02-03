# Init the atom particles

from initPositions import initPositions
from initVelocities import initVelocities
from calculateforces import calculateForces
import numpy as np

def initSimulation(particles):
    initPositions(particles);
    initVelocities(particles);
    particles.forces = calculateForces(particles.positions, particles.forces, np.array([0,0]), 0);