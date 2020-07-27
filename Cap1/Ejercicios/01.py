'''a) funcion convertir Fahrenheit a Celcius'''
#se define la funcion
def FaC(F):
    return (F-32)/1.8
#se ejecuta la funcion
F=int(input("\nTemperatura en F: "))
C=FaC(F)
print(f"Temperatura en C: {C}")


'''b) programa que sume numeros primos hasta n'''
#se ingresa el numero n
n=int(input("Ingrese el valor de n: "))
#inicializa la sumatoria en 0
sum=0
for num in range(2, n+1):
    i=2
    #se evalua si el numero es primo
    for i in range(2,num):
        if int(num%i)==0:
            i=num
            break;
    #si el numero es primo entonces se suma
    if i is not num:
        sum+=num 

print(f"La suma de los numeros primos hasta {n} es {sum}")


'''c) considerar tiples pitagoricos enteros positivos a,b,c tales que a^2 + b^2 = c^2, c=b+n
(n entero). Programa que halle todos los trples para un valor de n dado, donde a y b son menores 
o iguales al valor maximo m. Para n=1, hallar tiples con 1<=a<=100 y 1<=b<=100'''
#debe ir entre dos ciclos que recorran los valores de a y b
#ingresar el valor de n
n=int(input("\nValor de n: "))
m=int(input("Valor de m: "))

for a in range(1,m): #recorre los valores de a
    for b in range(1,m): #recorre los valores de b
        if a**2+b**2==(b+n)**2: #debe cumplir con la igualdad
            print(f"a={a}, b={b}, c={b+n}") #se presentan los valores de a, b ,c 


'''d) graficar'''


'''e) graficar'''
