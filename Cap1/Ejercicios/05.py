#Evaluar los limmites
from sympy import *
x=symbols('x')
#a)
print(limit(sin(x)/x,x,0))
#b)
print(limit(((x**3)+(3*(x**2))-5)/((2*(x**3))-(7*x)),x,oo))
#c)
print(limit((cos(x)+1)/(x-pi),x,pi))
#d)
print(limit(1/x,x,0,'+'))
#e)
print(limit(((2*sinh(x))-(2*sin(x)))/(cos(x)-1),x,0))
