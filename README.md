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
La Figura 1 es un diagrama de un ejemplo de SWAG con dos capas y la Figura 3 es un diagrama de un ejemplo de SWAG con cuatro capas.!
[r1](https://user-images.githubusercontent.com/91721507/194767980-0547dd8d-9607-4c49-953c-9229a6b3104b.PNG)
