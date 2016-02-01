# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:51:35 2016

@author: Mathijs
"""

import numpy as np
import config

def ComputeTemp(particles):
    # Using Boltzmann equipartition theorem
    T=config.mass * sum(sum(particles.velocities**2)) / ( 3*(config.nParticles - 1) * config.kB)
    return T

