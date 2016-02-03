# Plot results

import config
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numba import jit

@jit(nopython=True)
def corrHist(positions):
    g = np.zeros(config.histSteps);
    for p1 in range(1,config.nParticles):
        for p2 in range(p1):
            X = positions[p2,0] - positions[p1,0];
            Y = positions[p2,1] - positions[p1,1];
            Z = positions[p2,2] - positions[p1,2];
            
            X -= np.rint(X/config.lCalc) * config.lCalc;
            Y -= np.rint(Y/config.lCalc) * config.lCalc;
            Z -= np.rint(Z/config.lCalc) * config.lCalc;            
            
            distance = np.sqrt(X*X + Y*Y + Z*Z);
            for i in range(config.histSteps):
                if( (config.histRange/config.histSteps) * i < 
                    distance < (config.histRange/config.histSteps) * (i+1) ):
                        g[i] += 1 / ( 4 * np.pi * ((config.histRange/config.histSteps*i)**2) * (config.histRange/config.histSteps) );
                        break;    
                    
    g = g * 2 * (config.lCalc**3) / (config.nParticles*(config.nParticles-1));        
    return g, np.linspace( (config.histRange/config.histSteps), config.histRange, config.histSteps )
            
def plotResults(particles, temp, eK, eP):
    plt.figure(1)
    plt.title('Temperature')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), temp)
    
    plt.figure(2)
    plt.title('Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (K)')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eK, label="eK")
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eP, label="eP")
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eP+eK, label="eK+eP")
    plt.legend()
    
    plt.figure(3)
    plt.title('Correlation')
    plt.xlabel('Distance')
    plt.ylabel('g(r)')
    g, bins = corrHist(particles.positions)
    #plt.hist(g, config.histSteps, normed=1, facecolor='green', alpha=0.75)
    plt.plot(bins, g, 'r--', linewidth=1)
    
    
    
    plt.show();
    
    