#graficar
from sympy import *
from sympy.abc import x,y,t

x=Function('x')
deqn=Eq(x(t).diff(t,t)+5*x(t).diff(t)+6*x(t),0)
print(dsolve(deqn,x(t),ics={x(0):1, x.diff(t).subs(t,0):0}))