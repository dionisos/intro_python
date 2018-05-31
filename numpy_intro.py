"""

    Numerical Python (NumPy) fue escrito originalmente por Travis Oliphant para ser la base de un
    entorno de computación científica en Python (ahora se considera la base SciPy stack).
    Una de las razones para que sea tan importante NumPy radica en su manejo eficiente de arreglos ...
    ~ la vectorización de la información hace el código más conciso y fácil de leer

    Hay un gran diferencia en términos de desempeño y manipulación entre un arreglo y una lista/diccionario
    El objeto numpy.array a diferencia de Mathlab/R tiene un indexado zero-based
    Como en las listas y otras secuencias Python, se usa dos puntos (:) para indexar un rango de valores
    ~ la porción indexada de un arreglo se denomina 'slice'

"""

# Forma de importar para evitar conflictos p.e. from numpy import *
import numpy as np

arreglo = np.array([[1,2,3],[2,3,4]])
print("Dimensiones del Arreglo", arreglo.shape)
# Construir un arreglo aleatorio con dimiensiones específicas ...
arreglo = np.random.random((4, 4))
print(arreglo[2,:])
print(arreglo[:,1])

# Para ver información sobre la implementación de un arreglo p.e. print(c_array.flags)
print("Pruebas de rendimiento! ~ Arreglo 2D con 100 millones de datos ...")
c_array = np.random.rand(1000, 1000)
f_array = np.asfortranarray(c_array)

def sum_row(x) :
    return np.sum(x[0, :])

def sum_col(x) :
    return np.sum(x[:, 0])

# En un C-array los elementos en una fila están secuenciados (por columna no hay secuencia),
# mientras que en un F-array los elementos de una columna lo están ...
# Esto es de mucha importancia al diseñar algoritmos en Python

import time

start = time.time()
sum_row(c_array)
end = time.time()
suma_filas_carray = end - start

start = time.time()
sum_row(f_array)
end = time.time()
suma_filas_farray = end - start

start = time.time()
sum_col(c_array)
end = time.time()
suma_columnas_carray = end - start

start = time.time()
sum_col(f_array)
end = time.time()
suma_columnas_farray = end - start

print("Suma de filas Carray-Farray (seg.)", suma_filas_carray, "vs", suma_filas_farray)
print("Suma de columnas Carray-Farray (seg.)", suma_columnas_carray, "vs", suma_columnas_farray)


"""

    Existen dos maneras principales de acceder a información en un arreglo 'slicing' e 'indexing'
    Generalmente cortar (slicing) crea una vista de un arreglo e indexar crea una copia ...
    La función may_share_memory de NumPy permite determinar si dos arreglo son vistas ~ comparten memoria

    Ahora para crear arreglos NumPy existen varias alternativas:
    1. Utilizando la función 'array'
       ~ los argumentos de dicha función deben ser iterables u implementar __array__ (p.e. listas y tuplas);
         para arreglos multidimensionales las listas solamente deben estar anidadas
    2. Mediante 'arange' que combina la creación de una lista como rango y su paso a un arreglo
    3. Arreglo aleatorios mediante el módulo 'random' de NumPy
       ~ la función random() acepta una tupla como argumento y retornar un arreglo con dichas dimensiones
         mientras que rand() toma enteros como argumentos para dictar las dimensiones del arreglo :P
         randint() nos ayuda con la creación de listas de enteros del mismo modo

"""

# Los cambios en una vista afectan al otro arreglo ...
x = np.random.rand(30,4)
y = x[:5, :]
y[:] = 0
print(x[:5, :])
print("Comparten memoria:", np.may_share_memory(x, y))

# Para evitar dependencias es necesario primero crear un arreglo vacío mediante NumPy,
# Python entenderá al realizar operaciones que las referencias se deben mantener independientes!
# ~ las operaciones solamente se realizarán sobre los valores de los arreglos
x = np.random.rand(30,4)
y = np.empty([5, 4])
y[:] = x[:5, :]
y[:] = 0
print(x[:5, :])
print("Comparten memoria:", np.may_share_memory(x, y))

# Métodos de creación de arreglos NumPy a partir de listas ...
x = np.array([1, 2, 3])
y = np.array(['hello', 'world'])
x = np.array([[1, 2, 3],[4, 5, 6]])
x = np.arange(5)

# Métodos de creación de arreglos NumPy empleando aleatorios ...
# Creación de dos dimensiones cada una con tres filas y cinco columnas!
arreglo_aleatorio = np.random.rand(2, 3, 5)

# Arreglo mediante tupla con dos filas y tres columnas
shape_tuple = (2, 3)
arreglo_aleatorio = np.random.random(shape_tuple)

LOW, HIGH_EXCLUSIVE = 1, 11
SIZE = 10
arreglo_enteros = np.random.randint(LOW, HIGH_EXCLUSIVE, size=SIZE)
print("Tipo de información:", arreglo_enteros.dtype)


"""

    La ventaja de los arreglos NumPy radica en que se puede usar slicing e indexado para
    acceder a información y realizar cálculos manteniendo la eficiencia de los C-array
    Todas las operaciones están vectorizadas, se aplican a todo el arreglo en lugar de hacerlo por elementos
    ~ p.e. en un multiplicación se multiplican el primer elemento de cada arreglo, los segundos, etc.
    El performance es muy superior a diferencia de utilizar loops ...
    NumPy proporciona un conjunto de "funciones universales" a modo de evitar utilizar loops para optimizar
    http://docs.scipy.org/doc/numpy/reference/ufuncs.html

"""

x = np.array([1, 2, 3, 4, 5])
y = np.array([-1, 7, 3, 0, 2])

print("Multiplicación de vectores", x * y)
print("Comparación NumPy", x == y)
print("Funciones universales ...")
print("Cuadrados", np.square(x))
print("Mínimos", np.minimum(y, x))
print("Mediana", np.median(x))
# Incluso algunas operaciones disponen de otras de apoyo!
print("Acumulados", np.add.accumulate(x))
print("Matriz\n", np.multiply.outer(x, x))

"""

    Las operaciones de NumPy no es necesario realizarlas en vectores del mismo tamaño,
    no obstante es necesario conocer las reglas de 'broadcasting' que se aplican.

"""

"""
PENDIENTE
Broadcasting and shape manipulation
"""
