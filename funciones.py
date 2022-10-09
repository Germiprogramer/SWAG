#funcion para convertir lista de datos en rango(0,1)

lista = [1,3,4,6,7]

def rango01(lista):
    maximo = max(lista)
    minimo = min(lista)
    diferencia = maximo - minimo
    for i in range(len(lista)):
        lista[i] = (lista[i]-minimo) / diferencia

    return lista

#aplicamos la funcion a x1,x2, x3... usando for in range
def capa1(x):
    x = (2*x+3)/(x-1)
    

def x_1(x):
    return (x**1)

def x_2(x):
    return (x**2/2)

def x_3(x):
    return (x**3/6)

#def funcion():
