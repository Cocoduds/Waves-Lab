import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x1, y1 = np.loadtxt('thermal_4min_a.txt', unpack = True, skiprows = 3, max_rows =2401)




tao = 4 *600 #in deciseconds



#numeric integration
def area_t(a,b,dx):
    return ((a+b)/2)*dx
    
dx=np.diff(x1)
def integrate(y1,dx,tao):
    integral = 0
    for i in range(tao):
        integral = integral + area_t(y1[i+1], y1[i],dx[i]) 
    return(integral)

print(integrate(y1,dx,4))




#Finding an and bn
def an(n,tao,dx):
    y2_b= []
    for i in range (len(x1)):
        y2_b.append(y1[i]*np.cos(2*np.pi*n*x1[i]/tao))
    a = (2/tao)*integrate(y2_b,dx,tao)
    return a

def bn(n,tao,dx):
    y2_b= []
    for i in range (len(x1)):
        y2_b.append(y1[i]*np.sin(2*np.pi*n*x1[i]/tao))
    a = (2/tao)*integrate(y2_b,dx,tao)
    return a

Fourier = []
def series(Fourier,n,tao,dx):
    anlist=[]
    bnlist=[]
    for i in range(0,n+1):
        anlist.append(an(i,tao,dx))
        bnlist.append(bn(i,tao,dx))
    print(anlist)
    print(bnlist)
    for t in range(0,tao):
        sums = 0
        for i in range(1,n+1):
            sums = sums + (anlist[i]*np.cos(2*np.pi*i*x1[t]/tao)+bnlist[i]*np.sin(2*np.pi*i*x1[t]/tao))
        Fourier.append(anlist[0]/2+ sums)

t=np.linspace(0,tao)

print(an(0,tao,dx))
print(bn(1,tao,dx))
series(Fourier,3,tao,dx)
Fourier.append(0)
plt.plot(x1,Fourier)
plt.plot(x1,y1)
plt.show()
