#dados z1=1+i, z2=-2+i, z3=-i evaluar:
from sympy import *

z1=1+I
z2=-2+I
z3=-I
#z1+z2+z3
print(f"z1+z2+z3={z1+z2+z3}")
#z1z2/z3
print(f"z1z2/z3={(z1*z2)/z3}")
#e^z1
print(f"e^z1={exp(z1).expand(complex=True)}")
#ln(z1)
print(f"ln(z1)={log(z1)}")
pprint(ln(z1))
#sin(z3)
print(f"sin(z3)={sin(z3)}")