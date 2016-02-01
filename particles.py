#main data containing file for Argon

import config
import numpy as np

class Particles:
    positions = np.zeros(shape=(config.particles, 3),dtype="float64");
    velocities = np.zeros(shape=(config.particles, 3),dtype="float64");
    forces = np.zeros(shape=(config.particles, 3),dtype="float64");
    