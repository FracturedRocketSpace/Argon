# Main file for argon

# Import classes and functions
import config
import numpy as np
from particles import Particles
from initSimulation import initSimulation
from argonMove import argonMove
from checkResults import checkResults
from plotResults import plotResults
import timeit
from particlesanimation import animationPlot
from rescaleVelocity import rescaleVelocity
from calcResult import calcResult

# Start Timer
start = timeit.default_timer()

# Initialize position + velocity
particles = Particles(config.nParticles);
initSimulation(particles);

# Init check variables
temp = np.zeros(config.iterations);
eK = np.zeros(config.iterations);
eP = np.zeros(config.iterations);
pressure = np.zeros(config.iterations);
cV = np.zeros(config.iterations);

if(config.animation):
    anim = animationPlot();

# Main loop
for i in range(config.iterations):
    # Update position
    virial = argonMove(particles, eP, i);
    # Calculate temperature
    checkResults(particles, temp, eK, pressure, virial, cV, i);
    # Rescale 
    if ( (i+1) % config.rescaleIter == 0 and i < config.stopRescaleIter ):
        rescaleVelocity(particles, temp[i])
    #
    print("Iteration", i+1, "completed; Time is: ", round(i*config.dt, 3) );
    
    if(config.animation and i % config.animationIter == 0):
        anim.updateParticlePlot(particles);

for j in range( int( len(config.oscLength) ) ):
    print("Block length=",config.oscLength[j])       
    #Calculate the errors in pressure and cV        
    (pressureAvg, pressureError,cVAvg, cVError)=calcResult(pressure,cV,j)
    print("Compressibility factor=",pressureAvg,"; Error:",pressureError)
    print("cV=",cVAvg,"; Error:", cVError)

# Show program end
plotResults(particles, temp, eK, eP, pressure, cV)

# Stop timer
stop = timeit.default_timer()
print("Program ended in  =", int(stop - start), "seconds");
print(round( ((stop - start)/config.iterations)*1000 , 3 ), "ms per iteration for", config.nParticles, "particles")