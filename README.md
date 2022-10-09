# SWAG





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
