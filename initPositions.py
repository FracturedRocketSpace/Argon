# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:26:10 2016

@author: Mathijs
"""

import numpy as np
import config

def initPositions(particles):
    # Number and length of unit FCC unit cells    
    Nc=round( (config.nParticles/4)**(1/3) )
    Lcell=config.lCalc/Nc;
    
    
    # Positions of particles in FCC unit cell
    xCell=np.array([0, 0.5, 0.5, 0])
    yCell=np.array([0, 0.5, 0, 0.5])
    zCell=np.array([0, 0, 0.5, 0.5])
    
    # Generate position array
    n=0
    for x in range(Nc):
        for y in range(Nc):
            for z in range(Nc):
                for k in range(4):
                    particles.positions[n,0] = ( 0.25 + x + xCell[k] ) * Lcell #0.25 to prevent particles on boundary
                    particles.positions[n,1] = ( 0.25 + y + yCell[k] ) * Lcell
                    particles.positions[n,2] = ( 0.25 + z + zCell[k] ) * Lcell
                    n += 1
                    