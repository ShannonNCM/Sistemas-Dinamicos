from sympy import *

#derivadas de las funciones
x=symbols('x')
#hallar las derivadas
print(f"Derivadas")
#a
print(diff((3*x**3)+(2*x**2)-5,x))
#b
print(diff(sqrt(1+x**4),x))
#c
print(diff(exp(x)*sin(x)*cos(x),x))
#d
print(diff(tanh(x),x))
#e
print(diff(x**ln(x),x))

#hallar las integrales
print(f"\nIntegrales")
#a
print(integrate((3*x**3)+(2*x**2)-5,(x,0,1)))
#b
print(integrate(1/x**2,(x,1,oo)))
#c
print(integrate(exp(-x**2),(x,-oo,oo)))
#d
print(integrate(1/sqrt(x),(x,0,1)))
#e
print(integrate(sin(1/x)/x**2,(x,0,pi/2))) #esto no se si lo estoy haciendo bien hahah 
