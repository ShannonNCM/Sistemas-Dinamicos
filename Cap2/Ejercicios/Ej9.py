'''La razon a la que personas sanas se infectan es a veces su numero, la razon de recuperados y muertos
es b y c veces el numero de infectados. Inicialmente hay N personas saanas y ninguna enferma, numero de
muertes en un tiempo t?'''

from sympy import *
from sympy.abc import S,I,F,t,a,b,c,N

S=Function('S') #personas sanas
I=Function('I') #personas infectadas 
F=Function('F') #personas fallecidas
#se plantea el sistema de ecuaciones
eqsd=[Eq(S(t).diff(t),-a*S(t)+b*I(t)),Eq(I(t).diff(t),a*S(t)-b*I(t)-c*I(t)),Eq(F(t).diff(t),c*I(t))]
#se resuleve el sistema de ecuaciones
sol=dsolve(eqsd,[S(t),I(t),F(t)],ics={S(0):N,I(0):0})
pprint(sol)