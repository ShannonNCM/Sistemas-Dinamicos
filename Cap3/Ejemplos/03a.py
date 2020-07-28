'''Retrato de fase con cmapo vectorial'''

#librerias a utilizar
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

#sistema lineal
a,b,c,d=2,1,1,2
def dx_dt(x,t):
    return [a*x[0]+b*x[1],c*x[0]+d*x[1]]

#trayectorias en tiempo hacia adelante
ts=np.linspace(0,4,100)
ic=np.linspace(-1,1,5)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],'r-')

#trayectorias en tiempo hacia atras
ts=np.linspace(0,-4,100)
ic=np.linspace(-1,1,5)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],'r-')

#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-1,1)
plt.ylim(-1,1)

#campo vectorial
X,Y=np.mgrid[-1:1:10j,-1:1:10j]
u=a*X+b*Y
v=c*X+d*Y
pl.quiver(X,Y,u,v,color='b')
plt.show()