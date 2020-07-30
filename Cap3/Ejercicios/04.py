'''a) hallar los eigenvalores y eigenvectores de la matriz'''

#librerias a utilizar
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

#a)
#sistema
def dx_dt(x,t):
    return [0*x[0]+x[1],x[0]-x[1]+x[0]**3]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-3,3)
plt.ylim(-3,3)
#campo vectorial
X,Y=np.mgrid[-3:3:20j,-3:3:20j]
u=Y
v=X-Y+X**3
pl.quiver(X,Y,u,v,color='b')

plt.show()


#b)
#sistema
def dx_dt(x,t):
    return [-2*x[0]-x[1]+2,x[0]*x[1]]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-3,3)
plt.ylim(-3,3)
#campo vectorial
X,Y=np.mgrid[-3:3:20j,-3:3:20j]
u=-2*X-Y+2
v=X*Y
pl.quiver(X,Y,u,v,color='b')
plt.show()



#c)
#sistema
def dx_dt(x,t):
    return [x[0]**2-x[1]**2,x[0]*x[1]-1]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(-3,3,6)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"r-")
#etiquetas de ejes y estilo de letra
plt.xlabel('x',fontsize=10)
plt.ylabel('y',fontsize=10)
plt.tick_params(labelsize=10)
plt.xlim(-3,3)
plt.ylim(-3,3)
#campo vectorial
X,Y=np.mgrid[-3:3:20j,-3:3:20j]
u=-X**2-Y**2
v=X*Y-1
pl.quiver(X,Y,u,v,color='b')
plt.show()



#d)
