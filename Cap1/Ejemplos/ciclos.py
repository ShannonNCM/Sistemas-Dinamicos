#primeros n terminos de serie de fibonacci

#se define la funcion
def fibonacci(n):
    a, b=0, 1
    print(a)
    print(b)
    print(a+b)
    for i in range(n-3):
        a, b=b, a+b
        print(a+b)

#se ejecuta la funcion
fibonacci(20)
print()


#programa que sume los numeros naturales a n (sumatoria)
def sum_n(n):
    sum=0
    i=1
    while i<=n:
        sum+=i
        i+=1 #incremento
    print(f"La suma es: {sum}")

#ejecuta la funcion
sum_n(100)