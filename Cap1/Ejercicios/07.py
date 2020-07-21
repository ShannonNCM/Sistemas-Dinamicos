#graficar
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

#a
#establecer el dominio
x=np.linspace(-3,3,100)
#funcion a graficar
y=3*x**3+2*x**2-5
plt.plot(x,y)
plt.show()
#b
x=np.linspace(-5,5,100)
y=np.exp(-x**2)
plt.plot(x,y)
plt.show()

#c 
'''x,y=np.mgrid[-6:6:100j,-6:6:100j]
z=x**2-2*x*y-y**2-1
plt.contour(x,y,z, levels=[1,3,5,10])
plt.show()'''
#de forma mas cool
def f(x,y):
    return x**2-2*x*y-y**2-1
#contorno 2D
x,y=np.mgrid[-6:6:100j,-6:6:100j]
z=f(x,y)
plt.contour(x,y,z, levels=[1,3,5,10])
plt.show()
#para hacer contorno 3d
x=np.linspace(-6, 6, 30)
y=np.linspace(-6, 6, 30)
X,Y=np.meshgrid(x, y)
Z=f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z, 50, cmap='binary')
plt.show()
#en 3D la superficie
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis', edgecolor='none')
#plt.savefig('fig02.pdf')
plt.show()

#d
def f2(x,y):
    return 4*x**2*np.exp(y)-2*x**4-np.exp(4*y)
#contorno 2D
x,y=np.mgrid[-3:3:50j,-1:1:50j]
z=f2(x,y)
plt.contour(x,y,z, levels=[0.1,0.3,0.5,0.7,0.9])
plt.show()
#para hacer contorno 3d
x=np.linspace(-3, 3, 30)
y=np.linspace(-1, 1, 30)
X,Y=np.meshgrid(x, y)
Z=f2(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z, 50, cmap='binary')
plt.show()
#en 3D la superficie
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='plasma', edgecolor='none')
#plt.savefig('fig02.pdf')
plt.show()

#e
#grafica parametrica
t=np.linspace(-4,4,100)
x=t**2-3*t
y=t**3-9*t
plt.plot(x,y)
plt.show()