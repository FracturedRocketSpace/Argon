# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:02:21 2016

@author: Luka
"""

import config
import numpy as np

#@jit( nopython=True )
def ComputeEmean(velocities):
    return 0.5 * config.mass * np.sum(np.sum(velocities**2))/config.nParticles;

#@jit( nopython=True )
def ComputeE2mean(velocities):
    return np.sum((0.5 * config.mass * np.sum(velocities**2, axis=1))**2)/config.nParticles;

def calculateCv(velocities,temp):
    
    Emean = ComputeEmean(velocities);
    E2mean = ComputeE2mean(velocities);
    
    Cv = (E2mean - Emean**2)/(config.kB*temp**2);
    
    return Cv;