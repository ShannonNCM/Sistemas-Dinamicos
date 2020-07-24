#operacioes con matrices
import numpy as np

#escribimos las matrices
A=np.array([[1,2,-1],[0,1,0],[3,-1,2]])
B=np.array([[1,2,3],[1,1,2],[0,1,2]])
C=np.array([[2,1,1],[0,1,-1],[4,2,2]])
print(f"A={A} \nB={B} \nC={C}")
#a) A+4BC
print(f"A+4BC={A+(4*(np.dot(B,C)))}")
#b) inversa de la matriz
print(f"Inversa A: \n{np.linalg.inv(A)}")
print(f"Inversa B: \n{np.linalg.inv(B)}")
# print(np.linalg.inv(C)) como el dete es cero no tiene inversa
#c) A^3
pot=np.linalg.matrix_power(A,3)
print(f"A^3={pot}")
#d) det(C)
print(f"DetC= {np.linalg.det(C)}")
#e)eigenvalores y eigenvectores de B
print(f"{np.linalg.eig(B)}")