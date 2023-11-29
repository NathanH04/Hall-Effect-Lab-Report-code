# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:35:31 2023

@author: nphol
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


ydata = [0.457,0.885,1.332,1.782,2.242,2.716,3.191,3.697]
xdata = [5.03,9.99,15.00,19.98,25.00,30.02,34.92,40.0]

def line(x, a, b):
    return a*x+b
popt, pcov = curve_fit(line,xdata,ydata,sigma = [0.01 for  i in ydata])

slope = popt[0]
intercept = popt[1]
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1]))

best_fit = [slope*i + intercept for i in xdata]


fig = plt.figure(figsize = (5,5))
ax = fig.add_subplot(1,1,1)

ax.errorbar(xdata,
            ydata,
            marker = 'o',
            linestyle = 'none',
            color = 'black',
            capsize = 6
            )
ax.plot(xdata,best_fit, color = 'black')
ax.set_xlabel('Current / mA',fontsize = 15)
ax.set_ylabel('Voltage / V',fontsize = 15)
plt.tick_params(direction='in',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 10
                )
print(f'{slope*10**3}+-{err_slope*10**3}')
