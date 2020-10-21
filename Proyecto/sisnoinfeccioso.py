from sympy import *
from sympy.abc import x,y,t,b,g

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

#sistema SIS no infeccioso
#voy a tomar como valores
b=-1
g=-1
def dx_dt(x,t):
    return [ -b*x[0]+g*x[1] , b*x[0]-g*x[1] ]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
ic=np.linspace(0,100000,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(0,100000,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(0,100000)
plt.ylim(0,100000)
#campo vectorial
X,Y=np.mgrid[0:100000:20j,0:100000:20j]
u=-b*X+g*Y
v=b*X-g*Y
pl.quiver(X,Y,u,v,color='b')
plt.show()