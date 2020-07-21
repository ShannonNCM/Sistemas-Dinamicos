import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


#pleatear dos curvas en una grafica voltaje y tiempo
t=np.arange(0.0,2.0,0.01)
c=1+np.cos(2*np.pi*t)
s=1+np.sin(2*np.pi*t)
#caracterisitcas de la grafica
plt.plot(t,s,'r--',t,c,'b-.') #r-- da la linea roja discontinua y b-. la punteada con linea
plt.xlabel('tiempo (s)')
plt.ylabel('voltaje (mV)')
plt.title('Voltaje en funcion del tiempo')
plt.grid(True)
#plt.savefig("voltaje-tiempo.png") #guarda la figura
plt.show()

#graficar subgraficas
#dfine la funcion
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)
#caracteristicas de la grafica
plt.figure(1)
plt.subplot(211) #subplot(filas,col,numfig)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k',label='damping')
plt.xlabel("tiempo (s)")
plt.ylabel('amplitude (m)')
plt.title('pendulo amortiguado')
legend=plt.legend(loc='upper center',shadow=True)
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'g--',linewidth=4)
plt.xlabel('tiempo (s)')
plt.ylabel('amplitud (m)')
plt.title('pendulo no amortiguado')
plt.subplots_adjust(hspace=0.8)
plt.show()

#grafica de una superficie y contorno en 3D
alpha=0.7
phi_ext=2*np.pi*0.5
#se define la funcion
def flux_qubit_potential(phi_m,phi_p):
    return 2+alpha-2*np.cos(phi_p)*np.cos(phi_m)-alpha*np.cos(phi_ext-2*phi_p)

phi_m=np.linspace(0,2*np.pi,100)
phi_p=np.linspace(0,2*np.pi,100)
X,Y=np.meshgrid(phi_p,phi_m)
Z=flux_qubit_potential(X,Y).T

fig=plt.figure(figsize=(8,6))

ax=fig.add_subplot(1,1,1,projection='3d')
p=ax.plot_wireframe(X,Y,Z,rstride=4,cstride=4)
ax.plot_surface(X,Y,Z,rstride=4,cstride=4,alpha=0.25)
cset=ax.contour(X,Y,Z,zdir='z',offset=-np.pi,cmap=plt.cm.coolwarm)
cset=ax.contour(X,Y,Z,zdir='x',offset=-np.pi,cmap=plt.cm.coolwarm)
cset=ax.contour(X,Y,Z,zdir='y',offset=3*np.pi,cmap=plt.cm.coolwarm)

ax.set_xlim3d(-np.pi,2*np.pi)
ax.set_ylim3d(0,3*np.pi)
ax.set_zlim3d(-np.pi,2*np.pi)
ax.set_xlabel('$\phi_p$',fontsize=15)
ax.set_ylabel('$\phi_m$',fontsize=15)
ax.set_zlabel('Potencial',fontsize=15)
plt.tick_params(labelsize=15)
ax.set_title("Surface and contour plots",fontsize=15)
plt.show()

#grafica parametrica en 3d
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(1,1,1,projection='3d')
t=np.linspace(-10,10,1000)
x=np.sin(t)
y=np.cos(t)
z=t
ax.plot(x,y,z)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Parametric curve")
plt.show()

#grafica con animacion
fig=plt.figure()
ax=plt.axes(xlim=(0,2),ylim=(-2,2))
line=ax.plot([],[],lw=2)
plt.xlabel('time')
plt.ylabel('sin($\omega$t)')
#define la funcion
def init():
    line.set_data([],[])
    return line,
#funcion para animar
def animate(i):
    x=np.linspace(0,2,100)
    y=np.sin(2*np.pi*(0.1*x*i))
    line.set_data(x,y)
    return line,
anim=animation.FuncAnimation(fig,animate,init_func=init,frames=100,interval=200,blit=True)
plt.show()