'''uso de sympy'''

print(2/3+4/5)
from fractions import Fraction
print(Fraction(2,3)+Fraction(4,5))
#print(sqrt(16))
#print(sin(pi))

from sympy import *

x,y=symbols('x y')
fact=factor(x**3-y**3)
print(f"factoriza {fact}")
print(f"expande {expand(fact)}")
print(f"simplifica {factor(x**3-y**3)/(x-y)}")
print(f"fracciones parciales {apart(1/((x+2)*(x+1)))}") #fracciones parciales
print(f"simpl ftrig {trigsimp(cos(x)-cos(x)**3)}") #simplifica exp trig
print(f"limite {limit(1/x,x,oo)}") #limite
print(f"derivada {diff(x**2-3*x+6,x)}") #derivar
print(f"derivada parcial {diff(x**3*y**5,x,y,3)}") #derivar parcialmente
print(f"integral {integrate(sin(x)*cos(x),x)}") #integrar
print(f"integral definida {integrate(exp(-x**2-y**2),(x,0,oo),(y,0,oo))}")
print(f"expansion Taylor {(exp(x)*cos(x).series(x,0,10))}")
print(f"sumatoria (infinita) {summation(1/x**2,(x,1,oo))}")
print(f"raiz de ecuacion {solve(x**5-1,x)}")
print(f"resol ec simultaneas {solve([x+5*y-2,-3*x+6*y-15],[x,y])}")
z1=3+1*I
z2=5-4*I
print(f"complejos {z1, z2}") #I es el imaginario, se puede usar 1j
print(f"aritm complejos {2*z1+z1*z2}")
print(f"conjugado complejo {conjugate(z1)}")
print(f"argumento {arg(z1)}")
print(f"modulo {abs(z1)}")
print(f"parte real {re(z1)}")
print(f"parte imaginaria {im(z1)}")
print(f"expresar como x+iy {exp(I*z1).expand(complex=True)}")
A=Matrix([[1,-1],[2,3]])
B=Matrix([[0,2],[3,3]])
print(f"matriz 2x2 {A, B}")
print(f"algebra matrices {2*A+3*A*B}")
print(f"accesa primera fila {A.row(0)}")
print(f"transpuesta de matriz {A.T}")
print(f"segunda columna {A.T.row(1)}")
print(f"elmento fila1 col2 {A[0,1]}")
print(f"matriz inversa {A**(-1)}")
print(f"potencia matriz {A**5}")
print(f"determinante {A.det()}")
print(f"matriz ceros 3x3 {zeros(3,3)}")
print(f"matriz unos 1x5 {ones(1,5)}")
C=Matrix([[2,1,0],[-1,4,0],[-1,3,1]])
print(f"mat,riz 3x3 {C}")
print(f"row reduced echelon {C.rref()}")
print(f"eigenvalores {C.eigenvals()}")
print(f"eigenvectores {C.eigenvects()}")
s,t,w=symbols('s t w')
print(f"transf Laplace {laplace_transform(t**3,t,s)}")
print(f"transf inversa {inverse_laplace_transform(6/s**4,s,t)}")
print(f"transf Fourier {fourier_transform(-2*pi*abs(t),t,w)}")
print(f"tranff inv fourier {inverse_fourier_transform(1/(pi*w**2),w,t)}")