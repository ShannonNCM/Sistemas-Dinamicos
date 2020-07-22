'''se datan fosiles con la ecuacion dA/dt=-alfa*A, A cantidad de sustancia radioactiva 
remanente, alfa es constante, t en anios. Asumiendo a=1.5e-7, detemrinar edad de un fosil
contiene sustancia A con solo remanente de 30%'''

#se importan las librerias a utilizar
from sympy import *
from sympy.abc import t

#EDO
A=Function('A')
eq=A(t).diff(t)+1.5e-7*A(t)
sol=dsolve(eq,ics={A(0):1})
pprint(sol)
#resolviendo la ecuacion para hallar t en A=0.30
print(solve(exp((1.5e-7)*t)-0.30,t))
