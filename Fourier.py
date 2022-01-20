# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:58:16 2022

@author: dudle
"""

import numpy as np
import matplotlib.pyplot as plt

period = 240

Tmax = 100
Tmin=0
T=[]

Tfourier=[]

t=np.linspace(0,240,240)
for i in range(0,120,1):
    T.append(Tmax)
for i in range(120,240,1):
    T.append(0)

a0= 100
def bn(n):
    if n%2==0:
        return 0
    else:
        return 200/(n*np.pi)

def series(Tfourier,n):
    for t in range(0,240,1):
        sums = 0
        for i in range (n):
            print (i)
            sums = sums + bn(i+1)*np.sin((2*np.pi*(i+1)/period)*t)
        Tfourier.append(50+sums)
            
series(Tfourier,60)
plt.grid()
plt.xlabel("t")
plt.ylabel("T")  
plt.plot(t,T)  
plt.plot(t,Tfourier)
plt.show()
