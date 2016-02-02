# Plot results

import config
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plotResults(temp, eK, eP):
    plt.figure(1)
    plt.title('Temperature')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), temp)
    
    plt.figure(2)
    plt.title('Kinetic Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Kinetic Energy (K)')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eK)
    
    plt.figure(3)
    plt.title('Potential energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Potential Energy (K)')
    plt.plot( np.linspace(0, config.dt*config.iterations, config.iterations), eP)
    
    fig = plt.figure(4)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(particles.positions[:,0], particles.positions[:,1], -particles.positions[:,2], zdir='z', c= 'red')

    
    plt.show()