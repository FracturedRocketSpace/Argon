# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import config as c
from calculateforces import calculateForces

def move(particles):
    for p1 in range(c.nParticles):
        particles.positions[p1,:]+=particles.velocities[p1,:]*c.dt+0.5/c.mass*particles.force[p1,:]*c.dt**2
        particles.velocities[p1,:]+=0.5/c.mass*particles.force[p1,:]*c.dt
        calculateForces(particles)
        particles.velocities[p1,:]+=0.5/c.mass*particles.force[p1,:]*c.dt


    
    
    

      


