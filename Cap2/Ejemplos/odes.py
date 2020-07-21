from sympy import *
from sympy.abc import t 

#ode lineal de primer orden dI/dt=5sint-I/5
I=Function('I')
sol=dsolve(Eq(I(t).diff(t),5*sin(t)-I(t)/5),I(t))
pprint(sol)
print()

#ode segundo orden
I=Function('I')
sol=dsolve(Eq(I(t).diff(t,t)+5*I(t).diff(t)+6*I(t),10*sin(t)), I(t))
pprint(sol)