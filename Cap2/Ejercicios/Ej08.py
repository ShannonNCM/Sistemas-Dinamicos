'''dos tanques A y B de volumen V llenos con agua en t=0. volumen de sln v con m soluto fluye al tanque
A por segundo, la mezcla fluye de A a B a la misma razon y mezcla sale de B a la misma razon.'''

from sympy import *
from sympy.abc import A,B,t,v,m,V

A=Function('A')
B=Function('B')
#se plantea el sistema de ecuaciones diferenciales
eqsd=[Eq(A(t).diff(t)+(A(t)*v/V),m/V),Eq(B(t).diff(t)+(B(t)*v/V),A(t)*v/V)]
#se resuelve el sistema de edos con las condiciones iniciales
sol=dsolve(eqsd,[A(t),B(t)]) #no jala bien con condiciones iniciales
pprint(f"{ sol}")




#las soluciones estan dadas por:
S, I = symbols("S I", cls=Function)
t, b, g = symbols("t b g")
#se plantea el sistema de ecuaciones diferenciales
sis=[Eq(S(t).diff(t),b*S-g*I),Eq(I(t).diff(t),-b*S+g*I)]
#se resuelve el sistema de edos con las condiciones iniciales
sol=dsolve(sis,[S(t),I(t)])
pprint(f"{ sol}")