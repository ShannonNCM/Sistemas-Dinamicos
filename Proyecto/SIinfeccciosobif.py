from sympy import *
from sympy.abc import x,y,t,b,g

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl


#sistema
def dx_dt(x,t):
    return [ -1*x[0]*x[1] , 1*x[1]*x[0] ]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
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
        plt.plot(xs[:,0],xs[:,1],"r-")
#etiquetas de ejes y estilo de letra
plt.xlabel('S',fontsize=10)
plt.ylabel('I',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-4,4)
plt.ylim(-4,4)
#campo vectorial
X,Y=np.mgrid[-4:4:20j,-4:4:20j]
u=-1*X*Y
v=1*Y*X
pl.quiver(X,Y,u,v,color='b')
plt.savefig("SIinf.pdf")
plt.show()