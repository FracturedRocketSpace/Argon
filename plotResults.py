# Plot results

import config
import matplotlib.pyplot as plt

def plotResults(temp, eK, eP):
    plt.figure(1)
    plt.title('Temperature')
    plt.xlabel('Iteration')
    plt.ylabel('Temperature (K)')
    plt.plot(range(config.iterations), temp)
    
    plt.figure(2)
    plt.title('Kinetic Energy')
    plt.xlabel('Iteration')
    plt.ylabel('Kinetic Energy (K)')
    plt.plot(range(config.iterations), eK)
    
    plt.figure(3)
    plt.title('Potential energy')
    plt.xlabel('Iteration')
    plt.ylabel('Potential Energy (K)')
    plt.plot(range(config.iterations), eP)
    
    plt.show()