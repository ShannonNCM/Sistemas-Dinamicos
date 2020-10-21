import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl


def dF(r, theta):
    return [ r*(1-(np.cos(theta)*np.cos(theta))-r**2) , (1/2)*np.cos(theta)*np.sin(theta)-1 ]

X, Y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
u, v = np.zeros_like(X), np.zeros_like(X)
NI, NJ = X.shape

for i in range(NI):
    for j in range(NJ):
        x, y = X[i, j], Y[i, j]
        r, theta = (x**2 + y**2)**0.5, np.arctan2(y, x)
        fp = dF(r, theta)
        u[i,j] = (r + fp[0]) * np.cos(theta + fp[1]) - x
        v[i,j] = (r + fp[0]) * np.sin(theta + fp[1]) - y

plt.quiver(X, Y, u, v, color='b')
plt.streamplot(X, Y, u, v, color='r')
plt.axis('square')
plt.axis([-2.5, 2.5, -2.5, 2.5])
#agregando el circulo
phi = np.linspace(0, 2*np.pi, 200)
r = 0.5
x = r*np.cos(phi)
y = r*np.sin(phi)
plt.plot(x,y, color='g')
r = 2
x = r*np.cos(phi)
y = r*np.sin(phi)
plt.plot(x,y, color='g')
plt.show()