#programa que califica los resultados de estudiantes

#se define la funcion
def grade(score):
    if score>=70:
        letter='A'
    elif score>=60:
        letter='B'
    elif score>=50:
        letter='C'
    elif score>=40:
        letter='D'
    else:
        letter='F'
    return print(letter)

#se ejecutra la funcion
score=int(input("Nota: "))
grade(score)


'''computadora debe "pensar" en un entero aleatorio entre 1 y 20
y el usuario debe adivinar el numero en seis intentos, debe 
indicar si el intento es alto o bajo'''

import random

intentos=0
#numero entero entre 1 y 20
num=random.randint(1,20)
#intentos de adivinar el numero
while intentos<=6:
    guess=int(input("Ingrese un numero del 1 al 20: "))
    intentos+=1 #paso de iteraciones
    if guess<num:
        print("Su numero es muy bajo")
    if guess>num:
        print("Su numero es muy alto")
    if guess==num:
        break
if guess==num:
    print(f"El numero se encontro en {intentos} intentos")
else:
    print(f"No se encontro el numero, el numero es {num}")