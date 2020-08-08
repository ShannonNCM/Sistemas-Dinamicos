#serie de tiempo y retrato de fase para sistema depredador-presa.

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#modelo de Holling-Tanner
def HollingTanner(X,t=0):
    return [ X[0]*(1-X[0]/7)-6*X[0]*X[1]/(7-7*X[0]) , 0.2*X[1]*(1-0.5*X[1]/X[0]) ]

t=np.linspace(0,200,1000)
#valores iniciales x0=7, y0=0.1
Sys0=np.array([7,0.1])

X,infodict=integrate.odeint(HollingTanner,Sys0,t,full_output=True)
x,y=X.T

fig=plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace=0.5,hspace=0.3)
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

ax1.plot(t,x,'r-',label='presa')
ax1.plot(t,y,'b-',label='depredador')
ax1.set_title('Series de tiempo')

ax1.set_xlabel("Tiempo")
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x,y,color='blue')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Retrato de Fase')
ax2.grid()
plt.show()