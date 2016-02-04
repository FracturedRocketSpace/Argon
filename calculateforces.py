# calculateForce

import numpy as np
import config as c
from numba import jit

#calculate forces
@jit( nopython=True )
def calculateForces(positions, forces, eP, i):
    forces=np.zeros(shape=(c.nParticles,3))
    virial = 0;
    for p1 in range(c.nParticles):
        for p2 in range(c.nParticles):
            if p1 > p2:
                X = positions[p2,0] - positions[p1,0];
                Y = positions[p2,1] - positions[p1,1];
                Z = positions[p2,2] - positions[p1,2];
                
                X -= np.rint(X/c.lCalc) * c.lCalc;
                Y -= np.rint(Y/c.lCalc) * c.lCalc;
                Z -= np.rint(Z/c.lCalc) * c.lCalc;
                
                r2 = X*X + Y*Y + Z*Z;
                
                r2i = 1 / r2;
                
                r6i = r2i*r2i*r2i
                
                force = 24  * r6i * (2*r6i - 1) * r2i;
                eP[i] += 4 * r6i * (r6i - 1);
                virial +=np. sqrt(r2) * -force
                
                forces[p1,0] -= force * X;
                forces[p1,1] -= force * Y;
                forces[p1,2] -= force * Z;
                
                forces[p2,0] += force * X; 
                forces[p2,1] += force * Y; 
                forces[p2,2] += force * Z; 
    return forces, virial
            