import math

def rango01(lista):
  nueva = []
  maximo = max(lista)
  minimo = min(lista)
  diferencia = maximo - minimo
  for i in range(len(lista)):
    nueva.append((lista[i]-minimo) / diferencia)
  return nueva


def rango_max_min(nueva, original):
    nueva = rango01(nueva)
    for i in range(len(nueva)):
        nueva[i] = round(nueva[i]*(max(original)-1)+1,2)
    return nueva

def capa1(x):
  x = (2*x+3)/(x+2)
  return x

def capa2(x):
  x = round(math.sin(x**2),2)
  return x

def capa3(x):
  x = 1/math.log(x,10)
  return x 
  
def aplicar_capa1(lista):
  for i in range(len(lista)):
    lista[i] = capa1(lista[i])
  return lista

def aplicar_capa2(lista):
  for i in range(len(lista)):
    lista[i] = capa2(lista[i])
  return lista

def aplicar_capa3(lista):
  for i in range(len(lista)):
    lista[i] = capa3(lista[i])
  return lista

def x_1(lista):
    lista1 = []
    for i in range(0, len(lista)):
        lista1.append(lista[i])
    return lista1

def x_2(lista):
    lista2 = []
    for i in range(0, len(lista)):
        lista2.append(lista[i]**2/2)
    return lista2

def x_3(lista):
    lista3 = []
    for i in range(0, len(lista)):
        lista3.append(lista[i]**3/6)
    return lista3
