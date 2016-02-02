# Rescale the velocity

import config
import numpy as np

def rescaleVelocity(particles, temp):
    particles.velocities *= np.sqrt(config.tRescale/temp)