# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:41:08 2016

@author: Luka
"""

import matplotlib.pyplot as plt
import config

class animationPlot():
    def __init__(self):
        fig = plt.figure(4)
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlim(0,config.lCalc);
        self.ax.set_ylim(0,config.lCalc);
        self.ax.set_zlim(0,-config.lCalc);
        
        self.old = None

    def updateParticlePlot(self,particles):
        if self.old != None:
            self.ax.collections.remove(self.old);
        self.old = self.ax.scatter(particles.positions[:,0], particles.positions[:,1], -particles.positions[:,2], zdir='z', c= 'red')
        
        plt.show();
        plt.pause(0.001);