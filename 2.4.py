# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:39:10 2022

@author: dudle
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit
plt.close()

def fit_func(x,a,b,psi,d):
    return 20*np.sin(b*x+psi) + d
x1, y1 = np.loadtxt('thermal_1min_a.txt', unpack = True, skiprows = 3)
x2, y2 = np.loadtxt('thermal_1min_b.txt', unpack = True, skiprows = 3)
x3, y3 = np.loadtxt('thermal_2min_a.txt', unpack = True, skiprows = 3)
x4, y4 = np.loadtxt('thermal_2min_b.txt', unpack = True, skiprows = 3)
x5, y5 = np.loadtxt('thermal_4min_a.txt', unpack = True, skiprows = 3)
x6, y6 = np.loadtxt('thermal_4min_b.txt', unpack = True, skiprows = 3)
x7, y7 = np.loadtxt('thermal_6min.txt', unpack = True, skiprows = 3)
x8, y8 = np.loadtxt('thermal_8min.txt', unpack = True, skiprows = 3)
x9, y9 = np.loadtxt('thermal_16min.txt', unpack = True, skiprows = 3)


figure,axis = plt.subplots(3,3)
axis[0, 0].plot(x1, y1)
axis[0, 0].set_title("1 minute A")

axis[0, 1].plot(x2, y2)
axis[0, 1].set_title("1 minute B")

axis[0, 2].plot(x3, y3)
axis[0, 2].set_title("2 minute A")

axis[1, 0].plot(x4, y4)
axis[1, 0].set_title("2 minute B")

axis[1, 1].plot(x5, y5)
axis[1, 1].set_title("4 minute A")

axis[1, 2].plot(x6, y6)
axis[1, 2].set_title("4 minute B")

axis[2, 0].plot(x7, y7)
axis[2, 0].set_title("6 minute")

axis[2, 1].plot(x8, y8)
axis[2, 1].set_title("8 minute")

axis[2, 2].plot(x9, y9)
axis[2, 2].set_title("16 minute")




#a=1
#b=2*np.pi/2400
#psi=-90
#d=50
#
#popt,pcov = curve_fit(fit_func,x1,y1,p0=[a,b,psi,d], bounds=((-np.inf, -np.inf, -np.inf, 40), (np.inf, np.inf, np.inf, 60)) ,maxfev = 10000000)
#print (popt,pcov)
#plt.plot(x1,fit_func(x1,*popt),"-")


