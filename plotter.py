# Plotter&Saver
# Note: Plot shown on screen is different from plot saved to disk!

import scipy.io
import matplotlib.pyplot as plt
import matplotlib

print('Importing')
imp = scipy.io.loadmat('2016-02-25 140158.mat',squeeze_me=True) # ENTER FILENAME HERE!!!
for key,val in imp.items():
    exec(key + '=val')
print('Importing done!')

# Set Font
fontsize = 20 ;
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : fontsize}

matplotlib.rc('font', **font)

#
plt.figure(1)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Temperature $\left(\frac{\epsilon}{k_b}\right)$', fontsize=fontsize)
plt.plot(timeAxis , temp)
plt.savefig('Temperature.png', bbox_inches='tight')

plt.figure(2)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Energy ($\epsilon$)', fontsize=fontsize)
plt.plot( timeAxis, eK, label="eK")
plt.plot( timeAxis, eP, label="eP")
plt.plot( timeAxis, eP+eK, label="eK+eP")
plt.legend()
plt.savefig('Energy.png', bbox_inches='tight')

plt.figure(3)
plt.xlabel(r'Distance ($\sigma$)', fontsize=fontsize)
plt.ylabel('g(r)', fontsize=fontsize)
plt.bar(histAxis ,g, histAxis[0])
plt.savefig('Correlation.png', bbox_inches='tight')

plt.figure(4)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Compressibility factor $\left(\frac{V}{\sigma^3}\right)$', fontsize=fontsize)
plt.plot(timeAxis, pressure)
plt.savefig('Pressure.png', bbox_inches='tight')

plt.figure(5)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Cv $\left(\frac{k_b}{V}\right)$', fontsize=fontsize) # Units?
plt.plot(timeAxis, cV)
plt.savefig('Cv.png', bbox_inches='tight')

plt.figure(6)
plt.xlabel(r'Time ($\tau$)', fontsize=fontsize)
plt.ylabel(r'Displacement ($\sigma$)', fontsize=fontsize)
plt.plot(timeAxis, displacement)
plt.savefig('displacement.png', bbox_inches='tight')

plt.show();