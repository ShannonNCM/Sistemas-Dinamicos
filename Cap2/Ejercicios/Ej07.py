'''reacciona A conviertiendose en B a razon alfa veces la cantidad de A presente, B se convierte en C
a razon beta veces B. Inicialmente solo hay una cantidad M de A presente.'''
from sympy import *
from sympy.abc import A,B,C,t,a,b,M

A=Function('A')
B=Function('B')
C=Function('C')
#se plantean el sistema de ecuaciones diferenciales
eqsd=[Eq(A(t).diff(t),-a*A(t)),Eq(B(t).diff(t),a*A(t)-b*B(t)),Eq(C(t).diff(t),b*B(t))]
#se resuelve el sistema de edos con las condiciones iniciales
sol=dsolve(eqsd,[A(t),B(t),C(t)],ics={A(0):M,B(0):0,C(0):0})
pprint(f"{ sol}")