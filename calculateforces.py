# -*- coding: utf-8 -*-

import numpy as np
import config as c
import scipy.spatial.distance as sc

#calculate cell offset
def cellOffset(current,other):
    return np.around((current-other)/c.lCalc);

#calculate forces
def calculateForces(atoms):
    for p1 in range(0,c.nParticles):
        for p2 in range(0,p1):
            cell_offset = cellOffset(p1,p2);
            new_p2_position = atoms.positions[p2,:]+cell_offset*c.lCalc;
            r = sc.euclidean(atoms.positions[p1,:],new_p2_position);
            force = 24*c.epsilon/c.sigma*(atoms.positions[p1,:]-new_p2_position)*(2*(c.sigma/r)**14-(c.sigma/r)**8);
            atoms.forces[p1,:] += force;
            atoms.forces[p2,:] += -force;