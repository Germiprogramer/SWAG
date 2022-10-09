# SWAG

Los miembros del grupo son : Germán Llorente, Gonzalo Martínez, Alex Muñoz, Carlos Puigserver

https://github.com/Germiprogramer/SWAG.git

# Resumen del paper
## Introducción

El Deep learning permite modelos computacionales que se componen de múltiples capas de procesamiento y aprender representaciones muy abstractas de datos. Ha habido informes de muchos éxitos utilizando redes neuronales profundas (DNN) en diferentes  áreas. Estos DNN,  nos han permitido resolver problemas difíciles y ha motivado un extenso trabajo para comprender sus propiedades teóricas. 

El proceso de cómo entrenar efectivamente un DNN es una tarea complicada. Características como la naturaleza de las funciones de activación,las arquitecturas de red… pueden afectar el proceso de entrenamiento de una red neuronal.
En particular, algunas opciones de estas características pueden causar pérdida de información o pueden aumentar la cantidad de tiempo necesario para entrenar una DNN.
La cuestión de cómo encontrar efectivamente el mejor conjunto de funciones de activación no lineales es un desafío. Algunas de las funciones de activación no lineales más conocidas son:

sigmoid(x) = 1/(1 + e^−X )                        (1) 

tanh(x) = (1 − e^−2X )/(1 + e^−2X )               (2)

ReLU(x) = max(x; 0)                               (3)
 
 La función de activación en la ecuación (3) Unidad Lineal Rectificada (ReLU), es la más popular y la más utilizada.


Chung ha propuesto funciones de activación no lineales entrenables que utilizaron una aproximación de serie de Taylor de sigmoides, tanh y ReLU como un punto de inicialización para sus funciones de activación, y entrenaron los coeficientes de la aproximación de serie de Taylor para optimizar el entrenamiento. Esta implementación utilizó la misma función polinomial en cada neurona de una capa determinada. 

En este paper, presentamos un tipo de red neuronal en la que las funciones de activación en cada capa forman una base polinomial. 
También proponemos una nueva arquitectura en la que concatenamos verticalmente muchas capas completamente conectadas para formar una capa que hace que el cálculo sea más eficiente. 




## Representación de una función con una base

Supongamos que tenemos un conjunto de datos {xj} para 1 ≤ j ≤ n y etiquetas {yj} que corresponden a nuestro conjunto de datos. Queremos encontrar una función f(x) tal que f(xj) = yj para todo 1 ≤ j ≤ n. El teorema de aproximación de Stone-Weierstrass afirma que cualquier función continua de valor real en un conjunto compacto puede ser aproximada uniformemente por un polinomio. 
La simplicidad de los sistemas polinómicos los hace muy atractivos desde el punto de vista analítico y computacional. Son fáciles de formar y tienen propiedades bien entendidas. El uso de polinomios de un grado determinado como funciones de activación para todas las neuronas de una misma capa parece desaconsejarse matemáticamente en los entornos tradicionales de las redes neuronales porque no son aproximadores universales. El teorema de Leshno et al. (1993) implica que las redes neuronales totalmente conectadas con un número suficiente de número de neuronas son aproximadores universales si y sólo si las funciones de activación no son polinomios. Observamos que en esta configuración tradicional se supone que la función de activación es la misma para cada neurona de una capa determinada. Ahora damos la siguiente extensión del teorema de aproximación de Stone-Weierstrass:

![c1](https://user-images.githubusercontent.com/91721507/194769192-ab17cfbd-441c-4568-87d0-ffe78794a498.PNG)


Demostración. Obsérvese que {σp}^∞  desde p=0 es una base para el espacio vectorial de polinomios sobre R. Así que como sabemos sabemos que los polinomios son densos en C(Xn) por el teorema de aproximación de Stone-Weierstrass el resultado es el siguiente:

Este corolario implica que si permitimos un conjunto diverso de funciones de activación polinómica en
una capa particular seguiremos teniendo el resultado de la capacidad de aproximación universal de las redes neuronales feedfoward. Utilizando el mismo marco que Leshno et al. (1993), en el que la salida se suponía en Rn se puede obtener fácilmente una extensión a dimensiones superiores
redefiniendo σp{w} como una operación puntual que toma cada elemento de w y lo eleva al grado de p por ejemplo, dado w = [2, 3], entonces σ4{w} = [2^4, 3^4].






## Arquitectura de un algoritmo SWAG

Sea xj ∈ Rd un punto de datos en nuestro conjunto de datos {xj}j=1  n
0: Normalizar los datos en un intérvalo[0,1]
1: Crear la primera capa de polinomios como sigue:
  1.1: Elija un k para el número de términos polinómicos utilizados (k es un hiperparámetro del modelo).
  1.2: Elija l para el número de neuronas que corresponden a cada monomio de la 1ª capa (l es un hiperparámetro del modelo).
  1.3: Crear k capas totalmente conectadas con l neuronas en cada capa, todas con xj como entradas.
    1.3.1: La capa pª capa totalmente conectada para 1 ≤ p ≤ k está definida por σp{Wx + b} para W ∈ l × d, b ∈ Rl, y σp como se ha definido anteriormente.
    1.3.2: La inicialización de los pesos es aleatoria y se extrae de N (0, 1), una distribución gaussiana con media 0 y desviación estándar 1.
  1.4: Concatenar verticalmente las k capas para formar un vector de longitud l * k
2: Crear una capa con una función de activación lineal. Ésta se considera la segunda capa de SWAG.
3: Para añadir una tercera y cuarta capa, repita la estructura de las 2 capas anteriores con la entrada de la tercera capa como la salida de la segunda capa. Si se añade    una tercera y cuarta capa entonces la primera dimensión de la matriz utilizada en la segunda capa es un hiperparámetro del modelo.
4: Continúe añadiendo capas en este patrón como desee.
5: La matriz utilizada para la última capa de activación lineal tendrá como primera dimensión la dimensión del vector de salida
La Figura 1 es un diagrama de un ejemplo de SWAG con dos capas y la Figura 2 es un diagrama de un ejemplo de SWAG con cuatro capas.


![figura_1](https://user-images.githubusercontent.com/91721507/194767980-0547dd8d-9607-4c49-953c-9229a6b3104b.PNG)
![figura_2](https://user-images.githubusercontent.com/91721507/194768081-2c1be083-77aa-438d-a853-7bea9137acee.PNG)


## Resultados

Para nuestro experimento final, ejecutamos SWAG en el conjunto de datos de escritura manual de MNIST (LC10). El conjunto de datos de datos se compone de un total de 70.000 imágenes, todas las cuales son muestras únicas de escritura a mano de los números del 0 al 9. Aplanamos estas imágenes en vectores de tamaño (784, 1) y las utilizamos como entradas para una DNN tradicional, así como a SWAG. La DNN tradicional tenía tres capas ocultas. En la primera y segunda capa utilizamos ReLU como función de activación con 1024 neuronas en cada capa. En la tercera capa utilizamos Softmax como función de activación con 10 neuronas. Para nuestra implementación de SWAG, utilizamos l = 500, k = 7 y 2 capas. Utilizamos un conjunto de entrenamiento que consistía en 60.000 imágenes, y un conjunto de prueba que consistía en 10.000 imágenes. En el método tradicional obtuvimos una precisión en la prueba de 0,9767 después de 4 épocas. SWAG consiguió una precisión de prueba de 0,9787 después de 4 épocas. Los resultados se muestran en la Figura 15 y la Figura 16.



![figura_15_16](https://user-images.githubusercontent.com/91721507/194768640-bae49e9f-bf0c-4728-8460-3c8389426006.PNG)




## Discusión

En este trabajo, presentamos un conjunto de funciones de activación y una nueva arquitectura. Nombramos esto arquitectura SWAG. La primera capa de nuestra arquitectura tiene al menos k neuronas donde k es el grado del polinomio para la estimación de la función g(x) tal que g(xj) = yj para todo 1 ≤ j ≤ n; este capa tiene k funciones de activación diferentes {x^p/p!}^k , p=1
                          
La segunda capa es una capa totalmente conectada con una función de activación lineal.
A partir de aquí, hemos visto que  creando un conjunto de datos aleatorios con funciones no lineales muy complicadas y evaluamos la efectividad de SWAG, descubrimos que puede aproximar las funciones mejor que los métodos tradicionales de aprendizaje profundo.

Tambien observamos que hay muchos conjuntos de bases que pueden estimar una función con precisión arbitraria. Nuestra conjetura es que la base ortogonal proporcionará una ventaja en algunos casos. Por otra parte , creemos que una estimación de Taylor de nuestro conjunto de datos aumentará el rendimiento de SWAG después de la inicialización.

Además, encontramos especialmente interesante la cuestión de cómo implementar esta arquitectura en redes neuronales convolucionales y recursivas. Las redes neuronales convolucionales han superado la precisión lograda con redes neuronales completamente conectadas en el conjunto de datos MNIST y también reducen la cantidad de parámetros necesarios para entrenar una red neuronal completamente conectada.

Nuestra hipótesis es que implementar el marco SWAG en redes neuronales convolucionales y recursivas nos permitirá reducir aún más los parámetros, hacer que nuestro modelo converja aún más rápido y obtenga una mayor precisión que la que es posible actualmente.


# ALGORITMO SWAG CÓDIGO

El dataset escogido trata acerca de contraseñas. Hemos escogido este archivo csv porque tenemos diferentes variables con las que podemos trabajar las cuales dependen de un número bastante bajo, lo que nos facilita la tarea. El algoritmo SWAG nos permite "cifrar" nuestras contraseñas con distintas capas.

## EXPLICACIÓN DEL CÓDIGO

Debido a que en nuestro dataset no todas las contraseñas son numericas, al leerlo seleccionamos solo las filas que la columna "password" se pueda leer como un int. Ademas, debido a que tienen una longitud muy dispersa, seleccionamos solo las filas que la columna "length" sea mayor que 5 y menor que 8; y finalmente eliminamos los 0 para que estos no influyan en los calculos. 
```
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
```    
Utilizamos la siguiente función para alterar nuestros datos a un rango (0,1), tal y como se explica que se debe hacer en el paper anteriormente resumido.

     def rango01(lista):
       nueva = []
       maximo = max(lista)
       minimo = min(lista)
       diferencia = maximo - minimo
       for i in range(len(lista)):
         nueva.append((lista[i]-minimo) / diferencia)
       return nueva

Una vez hemos hecho esto con nuestros valores, transformamos cada uno en otros tres mediante esta formula xp = x^p/p¡, y luego los concatenamos. Esto lo haremos despues de aplicar cada funcion.
```
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
```    
A partir de ahí, empezamos a aplicar distintas "capas", cambiando los valores de las listas. Cada capa es una función numérica.

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

Tras aplicar todas las capas, volvemos al rango numérico inicial.

    def rango_max_min(nueva, original):
        nueva = rango01(nueva)
        for i in range(len(nueva)):
            nueva[i] = round(nueva[i]*(max(original)-1)+1,2)
        return nueva
