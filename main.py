from funciones import * 

lt = [1,4,5,9,7,8,11]
normalizada = rango01(lt)
x1 = x_1(normalizada)
x2 = x_2(normalizada)
x3 = x_3(normalizada)
x1+=x2
x1+=x3
x1.sort()
concatenada1 = []
for i in range(0,len(x1),int(len(x1)/5)):
    concatenada1.append(x1[i])
print("-----------Aplicamos capa 1-----------")
f1 = aplicar_capa1(concatenada1)
print(f1)
print("-----------Aplicamos capa 2-----------")
f2 = aplicar_capa2(f1)
print(f2)
print("-----------Aplicamos capa 3-----------")
f3 = aplicar_capa3(f2)
print(f3)
print(rango_max_min(f3, lt))