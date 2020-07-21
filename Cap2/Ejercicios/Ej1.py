#importan las librerias a usar
from sympy import *
from sympy.abc import x

#a)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),-y(x)/x) , y(x))
pprint(sol)
print()

#b)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),2*y(x)/x) , y(x))
pprint(sol)
print()

#c)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),y(x)/(2*x)) , y(x))
pprint(sol)
print()

#d)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),y(x)**2/x) , y(x))
pprint(sol)
print()

#e)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),-(x*y(x))/(x**2+y(x)**2)) , y(x))
print(sol)
print()

#f)
y=Function('y')
sol=dsolve(Eq(y(x).diff(x),y(x)/x**2) , y(x))
pprint(sol)