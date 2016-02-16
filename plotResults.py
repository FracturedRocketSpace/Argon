# Plot results

import config
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numba import jit
from datetime import datetime
import scipy.io

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
    return g
    
def dumpData(particles, temp, eK, eP, pressure, Cv, displacement, g, timeAxis, histAxis):
    scipy.io.savemat(datetime.now().strftime('%Y-%m-%d %H%M%S'), dict(temp=temp, eK=eK, eP=eP, cV=Cv, pressure=pressure, displacement=displacement, g=g, timeAxis=timeAxis, histAxis=np.linspace((config.histRange/config.histSteps), config.histRange, config.histSteps ) ) )
            
def plotResults(particles, temp, eK, eP, pressure, Cv, displacement):
    timeAxis = np.linspace(0, config.dt*config.iterations, config.iterations);
    histAxis = np.linspace((config.histRange/config.histSteps), config.histRange, config.histSteps );
    
    plt.figure(1)
    plt.subplot(231)
    plt.title('Temperature')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature')
    plt.plot(timeAxis , temp)
    
    plt.subplot(232)
    plt.title('Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eK, label="eK")
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eP, label="eP")
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eP+eK, label="eK+eP")
    plt.legend()
    
    plt.subplot(233)
    plt.title('Correlation histogram')
    plt.xlabel('Distance')
    plt.ylabel('g(r)')
    g = corrHist(particles.positions)
    plt.bar(histAxis ,g,config.histRange/config.histSteps)
    
    plt.subplot(234)
    plt.title('Pressure')
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure')
    plt.plot(timeAxis, pressure)
    
    plt.subplot(235)
    plt.title('Cv')
    plt.xlabel('Time (s)')
    plt.ylabel('Cv')
    plt.plot(timeAxis, Cv)
    
    plt.subplot(236)
    plt.title('Displacement')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement')
    plt.plot(timeAxis, displacement)
    
    plt.show();
    
    # Dump Data
    dumpData(particles, temp, eK, eP, pressure, Cv, displacement, g, timeAxis, histAxis)