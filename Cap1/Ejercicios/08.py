#resolver las ecuaciones diferenciales
from sympy import *
from sympy.abc import x,y,t

#a
y=Function('y')
deqn=Eq(y(x).diff(x),x/(2*y(x)))
print(dsolve(deqn,y(x),ics={y(1):1}))
#b
y=Function('y')
deqn=Eq(y(x).diff(x),-y(x)/x)
print(dsolve(deqn,y(x),ics={y(2):3}))
#c
y=Function('y')
deqn=Eq(y(x).diff(x),x**2/(y(x)**3))
print(dsolve(deqn,y(x),ics={y(0):1}))
#d
x=Function('x')
deqn=Eq(x(t).diff(t,t)+5*x(t).diff(t)+6*x(t),0)
print(dsolve(deqn,x(t),ics={x(0):1, x(t).diff(t).subs(t,0):0}))
#e
x=Function('x')
deqn=Eq(x(t).diff(t,t)+5*x(t).diff(t)+6*x(t),sin(t))
pprint(dsolve(deqn,x(t),ics={x(0):1, x(t).diff(t).subs(t,0):0}))