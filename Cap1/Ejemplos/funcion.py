#parte1

#funciones
#definicion de funciones
def f_mu(mu,x):
    return mu*x*(1-x)

#ejecuta la funcion
print(f_mu(2,0.8))


#conversion F a K
#se define la fucnion
def FaK(F):
    return (F+459.67)*(5/9)

#ejecutar la funcion
F=int(input("\nTemperatura en F: "))
K=FaK(F)
print(f"Temperatur en K: {K}")

