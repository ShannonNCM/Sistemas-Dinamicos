'''programa que plotee arboles fractales'''
#queda pendiente porque no le ententi

from turtle import *
setheading(90)
penup()
setpos(0,-250)
pendown()

#se define la fucnion
def arbol_fractal(long,nivel):
    #dibuja un fractal
    pensize(long/10)
    if long<20:
        pencolor("verde")
    else:
        pencolor("cafe")

    speed(0)
    if nivel>0:
        fd(long)
        rt(30)
        arbol_fractal(long*0.7,nivel-1)
        lt(90)
        arbol_fractal(long*0.5,nivel-1)
        rt(60)
        penup()
        bk(long)
        pendow()

#se ejecuta la funcion
arbol_fractal(200,10)