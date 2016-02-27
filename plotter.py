# Plotter&Saver
# Note: Plot shown on screen is different from plot saved to disk!

import scipy.io
import matplotlib.pyplot as plt
import matplotlib

print('Importing')
imp = scipy.io.loadmat('GasArgon.mat',squeeze_me=True) # ENTER FILENAME HERE!!!
for key,val in imp.items():
    exec(key + '=val')
print('Importing done!')

# Set Font
fontsize = 25;
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : fontsize}

matplotlib.rc('font', **font)

from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#
plt.figure(1)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Temperature $\left(\frac{\epsilon}{k_b}\right)$', fontsize=fontsize)
plt.plot(timeAxis , temp, linewidth=2)
plt.savefig('Temperature.eps', bbox_inches='tight', dpi=100)

plt.figure(2)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Energy ($\epsilon$)', fontsize=fontsize)
plt.plot( timeAxis, eK, linewidth=2, label="eK")
plt.plot( timeAxis, eP, linewidth=2, label="eP")
plt.plot( timeAxis, eP+eK, linewidth=2, label="eK+eP")
plt.legend()
plt.savefig('Energy.eps', bbox_inches='tight', dpi=100)

plt.figure(3)
plt.xlabel(r'Distance ($\sigma$)', fontsize=fontsize)
plt.ylabel('g(r)', fontsize=fontsize)
plt.bar(histAxis ,g, histAxis[0])
plt.savefig('Correlation.eps', bbox_inches='tight', dpi=100)

plt.figure(4)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Compressibility factor $\left(\frac{V}{\sigma^3}\right)$', fontsize=fontsize)
plt.plot(timeAxis, pressure, linewidth=2)
plt.savefig('Pressure.eps', bbox_inches='tight',  dpi=100)

plt.figure(5)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Cv $\left(\frac{k_b}{V}\right)$', fontsize=fontsize) # Units?
plt.plot(timeAxis, cV, linewidth=2)
plt.savefig('Cv.eps', bbox_inches='tight', dpi=100)

plt.figure(6)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Squared displacement ($\sigma^2$)', fontsize=fontsize)
plt.plot(timeAxis, displacement, linewidth=2)
plt.savefig('Displacement.eps', bbox_inches='tight',  dpi=100)

plt.show();