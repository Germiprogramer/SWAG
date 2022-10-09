# SWAG


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
