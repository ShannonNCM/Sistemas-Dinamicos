#graficando con python y matplotlib

import numpy as np
import matplotlib.pyplot as plt

#establece el dominio
x=np.linspace(-2,2,50)
#funcion
y=x**2
#grafica basica
plt.plot(x,y)
plt.show()

#dos elementos en una grafica
#establecer el dominio
t=np.linspace(0,100,1000)
#funciones
f1=np.exp(-0.1*t)*np.cos(t)
f2=np.cos(t)
#plt.plot(t,f1);plt.plot(t,f2)
#grafica con texto
plt.plot(t,f1,label='f1');plt.plot(t,f2,label='f2')
plt.xlabel('t');plt.ylabel('f(t)')
plt.legend()
plt.show()

#grafica con etiquetas y titulo
plt.xlabel('x');plt.ylabel('y');plt.title('y=x^2')
#cambiar grosor de linea y color
plt.plot(x,y,color='green',linewidth=4)
plt.plot(x,y)
plt.show()

#graficar funciones implicitas
x,y=np.mgrid[-5:5:100j,-5:5:100j]
z=x**2/4+y**2
plt.contour(x,y,z,levels=[1])
plt.show()

#grafica parametrica
t=np.linspace(0,np.pi,100)
x=0.7*np.sin(t+1)*np.sin(3*t)
y=0.7*np.sin(t+1)*np.sin(3*t)
plt.plot(x,y)
plt.show()