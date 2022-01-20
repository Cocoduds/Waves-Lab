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

def amplitude(y1):
    return((max(y1)-min(y1))/2)    

def calculateDgamma(tao,amplitude): #tao in mins
    D = (2*np.pi*1/(tao*60))*(7.87**2)/(2*np.log(amplitude/63.66)**2)
    return D

def calculateDphi(tao,phasedif,period): #tao in mins phi deciseconds
    D = (2*np.pi*1/(tao*60))*(7.87**2)/(2*(2*np.pi*phasedif/period)**2)
    return D

x1, y1 = np.loadtxt('thermal_4min_a.txt', unpack = True, skiprows = 3)
plt.plot(x1,y1, label='sampled data')

Tfourier=[]
T=[]
Tmax = 100
Tmin = 0
period = int(len(y1)/4)
halfperiod = int(period/2)

for i in range(0,4,1):
    for i in range(0,halfperiod,1):
        T.append(Tmax)
    for i in range(halfperiod,period,1):
        T.append(Tmin)

a0= 100
def bn(n):
    if n%2==0:
        return 0
    else:
        return 200/(n*np.pi)

def series(Tfourier,n):
    for t in range(0,len(y1),1):
        sums = 0
        for i in range (n):
            sums = sums + bn(i+1)*np.sin((2*np.pi*(i+1)/period)*t)
        Tfourier.append(50+sums)
            
series(Tfourier,1)
print(np.arctan2(0,200/(1*np.pi)))
print(bn(1))
#a=1
#b=2*np.pi/2400
#psi=-90
#d=50
#
#popt,pcov = curve_fit(fit_func,x1,y1,p0=[a,b,psi,d], bounds=((-np.inf, -np.inf, -np.inf, 40), (np.inf, np.inf, np.inf, 60)) ,maxfev = 10000000)
#print (popt,pcov)
#plt.plot(x1,fit_func(x1,*popt),"-")


plt.plot(x1,T, label='Ideal square wave')
plt.plot(x1,Tfourier, label='1th Harmonic')
plt.title("6 minute")
plt.xlabel('t(ds)')
plt.ylabel('T(C)')
plt.legend(loc = 'upper right')
plt.grid()
plt.show()
print('amplitude = ', amplitude(y1))
print('D Gamma = ', calculateDgamma(4, amplitude(y1)))
print('D Phi = ', calculateDphi(4, 1180, period))