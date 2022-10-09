#funcion para convertir lista de datos en rango(0,1)
def rango01(lista):
    maximo = lista.max()
    minimo = lista.min()
    diferencia = maximo - minimo
    for i in range(len(lista)):
        lista[i] = (lista[i]-minimo) / diferencia

    return lista
