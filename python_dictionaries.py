
"""

    Los diccionarios en Python tal y como en otros lenguajes nos permiten
    manejar información en la forma de estructuras key/value
    Los elementos son accesados por una 'llave' y no por posición como una lista!
    El orden de los elementos en un diccionario no tiene relevancia ...

    Para agregar nuevos elementos en un diccionario basta asignar una nueva llave.
    Si se desea acceder a los elementos basta con la notación ['key']
    Consultar una llave que no existe genera una excepción 'KeyError'

    Una vez que se ha elegido un tipo de dato para las llaves, no debe variar.
    Normalmente se utilizan cadenas para dicho propósito ...

"""

grade_dict = { 'Alan Anderson': 4.0, 'Betsy Baron': 2.8, 'Tom Swift': 3.5 }
grade_dict['Alan Anderson'] = 3.9
grade_dict['Carlos Soria'] = 3.7

# Cuando son iterados los diccionarios, retornan una serie de llaves ...
# Lo cual se puede utilizar para consultar los elementos del diccionario.
for key in grade_dict:
    print(key, '\t', grade_dict[key])

"""

    Un problema con los diccionarios es tratar de acceder a una llave que no existe.
    Una solución es buscar la llave antes de acceder a su valor mediante 'in',
    otra forma más eficiente es con el método get()

    El método items() regresa todo el contenido de un diccionario como una lista,
    cada elemento en esta lista es una dupla (key, value) ...
    Es un método útil si se desea iterar sobre los elementos de un diccionario.

"""

llave = 'Dionisos'
if llave in grade_dict.keys() :
    print(llave, 'tiene el grado', grade_dict[llave])

value = grade_dict.get(llave)
if value is None :
    print('No existe el elemento en el diccionario ...')

for k, v in grade_dict.items() :
    print('Key: {}, Value: {}'.format(k, v))

"""

    Otro tipo de colección de datos, relacionada con el diccionario es el Python Set.
    - Contiene elementos simples, tal y como las listas
    - Los elementos deben ser únicos. Agregar un valor que ya existe no tiene efecto.
    - Se puede obtener uniones e intersecciones de los mismo (como en matemáticas)
    - Utilizan llaves como los diccionario para definirse (las listas corchetes)
    - Cuando se define un set vacío hay que usar la función set(), importante!
    - El orden de los conjuntos no importa en términos de comparación ...

    Para agregar o eliminar elementos se usan add() y remove() respectivamente.
    Las operaciones entre conjuntos generan "sets" a su vez.

"""

empty_set = set()
numeros_suerte = { 3, 7, 11, 27, 9 }

beat_set = {'John', 'Paul', 'George', 'Pete'}
beat_set.remove('Pete')
beat_set.add('Ringo')

a_set = {1, 2, 3, 4, 5, 6}
b_set = {4, 5, 6, 10, 20}

print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set - b_set)

# Números primos mediante conjuntos ...
# Para crear un conjunto a partir de una lista, es necesario utilizar 'set'
nums = set(range(2, 20))
comps = {j for i in nums for j in range(i * i, 20, i)}

# Equivalente al anterior :P
# for i in nums :
#    for j in range(i * i, 20, j) :
#        comps.add(j)

primes = nums - comps
print('Primos:', primes)

"""

    Python puede crear matrices de dos dimensiones facilmente por inicialización.
    Las matrices pueden contener cualquier tipo de dato por supuesto.
    Una vez que se ha creado una matriz, se pueden asignar los elementos que
    se desee siempre y cuando los índices no salgan de rango (basados en cero) ...

    Es posible generar matrices irregulares sin problema alguno.

"""

list2D = [
            [1, 3, 2],
            [50, 50, 66],
            [-1, -2, -3]
         ]

mat =    [
            [-1, -2, -3],
            [10, 20],
            [1, 2, 3, 4, 5]
         ]

print("Longitudes:", len(mat), len(mat[0]), len(mat[1]), len(mat[2]))

"""

    THE PYTHON MATRIX PROBLEM
    En el siguiente ejercicio ocurre que Python crea una fila y después tres
    referencias a la misma, en lugar de tener tres filas distintas ¬¬
    Para resolver éste problema hay que construir la lista multidimensional a pie :P

"""

mat = [ [0] * 3 ] * 3
mat[0][0] = 555
print(mat)

# Forma correcta de generar la matriz multidimensional ...
mat_solution = [[0] * 3  for i in range(3)]
mat_solution[0][0] = 555
print(mat_solution)

# Matriz de tres dimensiones ('_' indica una variable en blanco)
mat_3d = [[[0] * 2 for _ in range(2)] for _ in range(2)]
print(mat_3d)

rows = cols = 3
matriz = [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows)]
print(matriz)


"""
Python Without Fear - Brian Overland
Ed. Addison-Wesley Professional 2017
SECUENCIA
python_classes.py
"""
