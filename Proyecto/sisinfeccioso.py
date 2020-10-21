from sympy import *
from sympy.abc import x,y,t,b,g

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

b=-0.7
g=1
#sistema SIS infeccioso
#voy a tomar como valores de b=0.5
def dx_dt(x,t):
    return [ -b*x[0]*x[1]+g*x[1] , b*x[0]*x[1]-g*x[1] ]
#trayectorias en tiempo hacia adelante
'''ts=np.linspace(0,10,500)
ic=np.linspace(-4,4,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(-4,4,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")'''
#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-4,4)
plt.ylim(-4,4)
#campo vectorial
X,Y=np.mgrid[-4:4:20j,-4:4:20j]
u=-b*X*Y+g*Y
v=b*X*Y-g*Y
pl.quiver(X,Y,u,v,color='b')
plt.show()