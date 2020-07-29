'''hallar los puntos criticos dx/dt=x(1-x/2-y)  dy/dt=y(x-1-y/2)'''

#librerias a utilizar
from sympy import *

x,y=symbols('x,y')
P=x*(1-x/2-y)
Q=y*(x-1-y/2)

#establecer P(x,y)=0 y Q(x,y)=0
Peqn=Eq(P,0)
Qeqn=Eq(Q,0)
pcriticos=solve((Peqn,Qeqn),x,y)
print(pcriticos)