import math
import pandas as pd

def contrasena():
    df = pd.read_csv('common_passwords.csv')
    df = df[df['length']<8]
    df = df[df['length']>5]
    contrasenas = list(df['password'])
    i = 0
    while i<len(contrasenas):
        try:
            contrasenas[i] = int(contrasenas[i])
        except:
            contrasenas.remove(contrasenas[i])
        else:
            if contrasenas[i] == 0:
                contrasenas.remove(contrasenas[i])
            else:
                i=i+1
    return contrasenas
        

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
        nueva[i] = int(nueva[i]*(max(original)-1)+1)
    return nueva

def capa1(x):
  x = (2*x+3)/(x+2)
  return x

def capa2(x):
  x = math.sin(x**2)
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

def separar_y_concatenar(lista):
    x1 = x_1(lista)
    x2 = x_2(lista)
    x3 = x_3(lista)
    x1 += x2
    x1 += x3
    x1.sort()
    concatenada = []
    for i in range(0, len(x1), 3):
        concatenada.append(x1[i])
    return concatenada