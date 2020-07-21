'''un circuito en serie capacitor-resitor esta dado por: RdQ/dt + Q/C = E donde Q es la
carga del capacitor. R=1/(5+t) y capacitancia C=0.5, E=100. Hallar carga del capactiro
en Q(0)=0'''

#importando las librerias
from sympy import *
from sympy.abc import t

#resolviendo la ecuacion diferencia
Q=Function('Q')
eqd1=(1/(5+t))*Q(t).diff(t)+Q(t)/0.5-100
pprint(dsolve(eqd1 , ics={Q(0):0}))
print()

