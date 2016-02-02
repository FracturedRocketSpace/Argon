# -*- coding: utf-8 -*-

import numpy as np
import config as c
import scipy.spatial.distance as sc

#calculate cell offset
def cellOffset(current, other):
    return np.around((current-other)/c.lCalc);

#calculate forces
def calculateForces(particles):
    particles.forces=np.zeros(shape=(c.nParticles,3), dtype="float")
    for p1 in range(c.nParticles):
        for p2 in range(p1):
            cell_offset = cellOffset(particles.positions[p1,:], particles.positions[p2,:]) ;
            new_p2_position = particles.positions[p2,:]+cell_offset*c.lCalc;
            r = sc.euclidean(particles.positions[p1,:],new_p2_position);
            force = 24 * c.epsilon / c.sigma * (particles.positions[p1,:]-new_p2_position) * (2*(c.sigma/r)**14-(c.sigma/r)**8);
            particles.forces[p1,:] += force;
            particles.forces[p2,:] += -force;