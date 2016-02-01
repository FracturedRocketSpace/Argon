# Argon

1) Interactions between Argon atoms
Lennard-Jones potential

2) How do we move the atoms around?
r(t+dt) = r(t)+v(t)*dt+0.5*a(t)*dt^2
Velocity Verlet algorithm:
v(t+dt) = v(t)+0.5*(a(t+dt)+a(t))*dt

3) Boundary conditions
For particles colliding with the boundary:
Energy loss/gain (we can approximate with reflection, taking the average of the current and boundary energy)
Particle loss/gain

4) Initial conditions
Uniform distribution for the positions
Maxwell-Boltzmann distribution for the speeds
