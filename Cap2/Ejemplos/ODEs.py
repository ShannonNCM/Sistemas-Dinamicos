from sympy import *
from sympy.abc import t #con esto queda definida t como symbolo

#Ejemplo variables separables dx/dt = -t/x
t=symbols('t')
x=symbols('x',cls=Function)
sol=dsolve(Eq(x(t).diff(t),-t/x(t)),x(t))
print(sol)
print()

#Ejemplo variables separables dx/dt=t/x^2
t=symbols('t')
x=symbols('x',cls=Function)
sol=dsolve(Eq(x(t).diff(t),t/(x(t)**2)),x(t))
print(sol)
print()

#Ejemplo dP/dt = P(beta-deltaP)
t=symbols('t')
P=symbols('P',cls=Function)
b=symbols('b')
d=symbols('d')
sol=dsolve(Eq(P(t).diff(t),P(t)*(b-d*P(t))),P(t))
print(sol)
pprint(sol)
print()

#Ejemplo solucion series de potencias dx/dt +tx = t^3
#from sympy.abc import t#de esta forma se declara la variable simbolica para muchas variables simbolicas
x=Function('x')
eqd1=x(t).diff(t)+t*x(t)-t**3 #esta forma para igualar a cero (creo)
pprint(dsolve(eqd1,hint='1st_power_series',n=6,ics={x(0):1})) 
#hint es el metodo que se quiere que se use
#ics es el set de condiciones iniciales/frontera
#n da el exponente de la variable dependiente al que se va a evaluar

#Ejemplo solucion series de potencias segundo orden d^2x/dt^2 + 2t^2dx/dt + x =0
x=Function('x')
eqd2=x(t).diff(t,2)+2*t**2*x(t).diff(t)+x(t)
pprint(dsolve(eqd2,hint='2nd_power_series_ordinary',n=6))