'''usar bucle while para programar algoritmo Euclidiano para hallar el mayor comun divisor de dos
enteros. Hallar maximo comun divisor de 12348 y 14238'''

def EAlg(A,B):
    while B!=0:
        R=A%B
        A=B
        B=R
    print(f"El maximo comun divisor es {A}")

#pide que ingresen los valores de A y B
A=int(input("Ingrese entero A: "))
B=int(input("Ingrese entero B: "))
#se llama a la funcion
EAlg(A,B)