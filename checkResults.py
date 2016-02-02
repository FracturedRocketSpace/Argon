# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:51:35 2016

@author: Mathijs
"""

import numpy as np
import config
import scipy.spatial.distance as sc
from calculateforces import cellOffset


def ComputeTemp(particles, eK):
    # Using Boltzmann equipartition theorem
    T=2*eK / ( 3*(config.nParticles - 1) * config.kB)
    return T

def ComputeeK(particles):
    eK=0.5*config.mass* sum(sum(particles.velocities**2))
    return eK
    
def ComputeeP(particles):
    eP=0
    for p1 in range(0,config.nParticles):
        for p2 in range(0,p1):
            cell_offset = cellOffset(p1,p2);
            new_p2_position = particles.positions[p2,:]+cell_offset*config.lCalc;
            r = sc.euclidean(particles.positions[p1,:],new_p2_position);
            V= 4*config.epsilon*((config.sigma/r)**12-(config.sigma/r)**6);
            eP += V
    return eP
    
def checkResults(particles, temp, eK, eP):
    eK=ComputeeK(particles)
    temp=ComputeTemp(particles, eK)
    eP=ComputeeP(particles)
    