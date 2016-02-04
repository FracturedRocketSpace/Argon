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
        plt.ion()
        plt.show()        
        
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlim(0,config.lCalc);
        self.ax.set_ylim(0,config.lCalc);
        self.ax.set_zlim(0,-config.lCalc);
        
        self.angle=0;
        
        self.old = None
        
    def changeAngle(self):
        self.angle = (self.angle + config.animationRotation) % 360;
        self.ax.view_init(30,self.angle)
        

    def updateParticlePlot(self,particles):
        if self.old != None:
            self.ax.collections.remove(self.old);
        self.old = self.ax.scatter(particles.positions[:,0], particles.positions[:,1], -particles.positions[:,2], zdir='z', c= 'red')   
        
        self.changeAngle()      
        
        plt.draw();
        plt.pause(0.00001);