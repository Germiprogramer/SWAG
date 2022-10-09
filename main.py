lista = [1,3,4,6,7,9,11]

def rango01(lista):
    maximo = max(lista)
    minimo = min(lista)
    diferencia = maximo - minimo
    for i in range(len(lista)):
        lista[i] = (lista[i]-minimo) / diferencia

    return lista
  
def rango_max_min(lista):
  

#aplicamos la funcion a x1,x2, x3... usando for in range
def capa1(x):
  x = (2*x+3)/(x+2)
  return x
    
def aplicar_capa(lista):
  for i in range(len(lista)):
    lista[i] = capa1(lista[i])
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

print(rango01(lista))
x1 = x_1(lista)
x2 = x_2(lista)
x3 = x_3(lista)
print(x1)
print(x2)
print(x3)
x1+=x2
x1+=x3
x1.sort()
print(x1)
concatenada1 = []
for i in range(0,len(x1),int(len(x1)/5)):
    concatenada1.append(x1[i])
print(concatenada1)
print(aplicar_capa(concatenada1))

