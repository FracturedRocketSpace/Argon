#main data containing file for Argon

import config
import numpy as np

class Particles:    
    def __init__(self, nParticles):
        self.positions = np.zeros(shape=(nParticles, 3),dtype="float64");
        self.velocities = np.zeros(shape=(nParticles, 3),dtype="float64");
        self.forces = np.zeros(shape=(nParticles, 3),dtype="float64");