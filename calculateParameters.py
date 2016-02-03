# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:23:58 2016

@author: Mathijs
"""

import numpy as np
import config as c

def calculateParameters(particles, temp, i):
    virial=0
    for p1 in range(c.nParticles):
        for p2 in range(c.nParticles):
            if p1 > p2:
                X = particles.positions[p2,0] - particles.positions[p1,0];
                Y = particles.positions[p2,1] - particles.positions[p1,1];
                Z = particles.positions[p2,2] - particles.positions[p1,2];
                
                X -= np.rint(X/c.lCalc) * c.lCalc;
                Y -= np.rint(Y/c.lCalc) * c.lCalc;
                Z -= np.rint(Z/c.lCalc) * c.lCalc;
                
                r = np.sqrt( X*X + Y*Y + Z*Z );
                r2 = X*X + Y*Y + Z*Z;
                r2i = 1 / r2;
                r6i = r2i*r2i*r2i                
                force = 24  * r6i * (2*r6i - 1) * r2i;
                
                virial += r * -force
    Pressure=c.kB*temp[i] - 1/(3*c.nParticles)*virial
    return Pressure
