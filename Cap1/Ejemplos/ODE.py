from sympy import *
#from sympy import dsolve, Eq, symbols, Function, exp


#programa que resuelva la ODE dx/dt+x=1
t=symbols('t')
x=symbols('x',cls=Function)
deqn1=Eq(x(t).diff(t),1-x(t))
sol1=dsolve(deqn1,x(t))
print(sol1)
print()

#resuelve ODE d^2y/d^2t + dy/dt +y =e^t
t=symbols('t')
y=symbols('y',cls=Function)
deqn2=Eq(y(t).diff(t,t)+y(t).diff(t)+y(t),exp(t))
sol2=dsolve(deqn2,y(t))
print(sol2)
print()


#Ejemplo01 variables separables dx/dt = -t/x
t=symbols('t')
x=symbols('x', cls=Function)
deqn3=Eq(x(t).diff(t),(-t)/x(t))
sol3=dsolve(deqn3,x(t))
print(sol3)
print()
