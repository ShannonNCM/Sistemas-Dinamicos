'''a)temperatura inicial 75F, luego de una hora es 70F. Si la temperatura del cuarto 
es constante de 68F, cuanto tiempo antes de la primera lectura de temperatur ocurrio 
el asesinato? dT/dt=beta(T-T_R)'''

from sympy import *
from sympy.abc import t

#resolviendo la ecuacion diferncial
T=Function('T')
b=symbols('b')
eqd1=T(t).diff(t)-(b*(T(t)-68))
pprint(dsolve(eqd1 , ics={T(0):75}))
#encontrando el valor de la constante b
print(solve((7*exp(b*1))+68-70, b)) #esto sale como log pero es ln
#tiempo del asesinato (temperatura corporal normal es 98F)
t=symbols('t')
print(solve(7*exp(-1.25*t)+68-99 , t)) #por alguna razon no lo jala... :c
#no funcionaba porque tenia muchos decimales LOL


'''b)eq dif para moedelar la concentraciond e glucosa en la sangre g(t) esta dada por
dg/dt+kg=G/100V. k es constante, G razon ala que ingresa glucosa, V volumen de sange en
el cuerpo, resolver la ec diferencial'''
g=Function('g')
k=symbols('k')
G=symbols('G')
V=symbols('V')
pprint(dsolve(g(t).diff(t)+k*g(t)-(G/(100*V))))
