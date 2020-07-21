import numpy as np

a=np.arange(5)
b=np.arange(6).reshape(2,3)
print(f"a= {a}")
print(f"b=\n {b}")
A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])
print(f"prod elementos\n {A*B}")
print(f"prod matrices\n {A.dot(B)}")
print(f"prod matriz (punto)\n {np.dot(A,B)}")
c=np.arange(12).reshape(3,4) #arreglo 2d
print(f"arreglo 2d\n {c}")
print(f"suma columnas\n {c.sum(axis=0)}")
print(f"minimo de c/fila {c.min(axis=0)}")
print(f"suma acum de c/fila\n {c.cumsum(axis=1)}")
print(f"{np.linspace(0,2,5)}")
