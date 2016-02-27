# Config file 

# Animiation
animation = False;                                      # Set animation on or off. Setting the animation on increases simulation time
animationIter = 10;                                     # Iterations between updating animation
animationRotation = 0.50;                               # Animation rotation rate

# Simulation
nParticles = 4 * (6**3);                                # Number of particles. To fill a complete grid it should be set to 4 ** (n**3)
iterations = 6000;                                      # Number of iterations
tInitial = 2;                                           # Initial temperature
tRescale = tInitial;                                    # Rescale temperature
rescaleIter = 20;                                       # Iterations between rescale
stopRescaleIter = 1000;                                 # Iteration after which the rescaling stops
rho=1.2;                                                # Density in reduced units
dt = 0.004;                                             # Time step per iteration

# Parameters derived from other settings
lCalc =  (1/rho)**(1/3)*(nParticles/4)**(1/3)*2**(2/3); # Calculation domain length
a=(tInitial)**(1/2);                            # Used for Maxwell distribution

# Post processing and plots
oscLength=[50, 100, 150, 200, 250, 300, 500];           # Block lengths for error calculation
cVLength=250;                                           # Running average length for cV plot
histRange = (2)**(1/2) * (lCalc) * 3/5;                 # Maximum distance over which the pair correlation is determined          
histSteps = 150;                                        # Number of intervals for pair correlation