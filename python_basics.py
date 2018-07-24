"""

Python fue inventando en 1991 por el programador holandés Guido Van Rossum
Suele considerarse un "lenguaje prototipo", una vez diseñada una solución
o algoritmo se suele pasar a C/C++ si es que se desea más performance ...

Existen varias caracteristicas que lo diferencian de otros lenguajes, entre ellas:
- El manejo númerico es impresionante, considerando matrices y números complejos p.e.
- Se dispone de "enteros infinitos" es decir no hay límite (sólo por hardware) :P
- No existen bloques de código ni sentencias begin/end todo es por indentación!
- Las variables no son declaradas, se crean al asignarles un valor ...
- Python trata cada variable como una referencia!
- Todas las variables Python son alias (apuntadores), importante!!

"""

a, b, c = -100, 123, 456 # Asignación en Tupla
numero = ((10 - 5) * 3) ** 4
print (numero)

def convert(fahrenheit) :
    celsius = fahrenheit * 1.8 + 32.0
    return celsius

grados_fahr = float(input('Grados fahrenheit a convertir: '))
print ('Equivale en grados Celsius a ' + str(convert(grados_fahr)))

especificacion_formato = 'The numbers are {} and {}.'
cadena_salida = especificacion_formato.format(10, 20)
print(cadena_salida)

from math import pi

radio = 5.15
area = pi * (radio ** 2)
print(area)

def check_range(number) :
    if number < 1 :
        print('n is below range 1 to 300')
    elif number > 1 and number < 300 :
        print('number is beetwen 1 and 300')
        print('Thank you')
    else :
        print('number is above 300')

a = b = contador = 1
while a <= 1350 :
    a, b = a + b, a
    print(a, end=' ')
    if contador == 10:
        break
    contador += 1

"""

    Una lista Python es un conjunto ordenado de información (mutable)
    Puede contener cualquier tipo de dato, incluyendo otras listas a su vez ...
    Para agregar más elementos a una lista se utiliza el método append()
    Del mismo modo para eliminar elementos es empleado remove()
    Es posible comparar listas simplemente utilizando el operador ==

"""

temp_list = [79, 79, 80, 68, 79, 68, 80, "Dionisos", 3.1416]
temp_list.append(85)
print('\nComparativa (==) ' + str([77, 80, 85] == [77, 80, 80 + 5]))

# Todas las variables son referencias, importante no olvidar!
temp_list_copy = temp_list
temp_list.append('Brian')
print('Comparativa: ' + str(temp_list_copy == temp_list))

beat_list = ['Ringo', 'Paul', 'George', 'John', 'Dionisos']
beat_list.remove('Dionisos')
# Para copiar una lista elemento por elemento se puede utilizar 'slicing'
beat_list_ordenada = beat_list[:]
beat_list_ordenada.sort()

print(beat_list)
print(beat_list_ordenada)

producto = 1
number_list = [1, 13, 7, 9, 11, 14]
for number in number_list :
    producto *= number

cels_list = [15, 20, 25, 30, 7, -13, 1]

fahr_list = []
for celsius in cels_list :
    fahrenheit = celsius * 1.8 + 32.0
    fahr_list.append(fahrenheit)

"""

    Si se utilizan índices negativos se hace referencia a los elementos al revés,
    por ejemplo con un -1 se hace referencia al último elemento de la lista!
    Python soporta la técnica 'slicing' la cual permite acceder a un subconjunto
    de elementos en lugar de manejar un elemento a la vez (lectura/escritura)
    Con la técnica del 'slicing' se obtiene una nueva lista con las opciones:

    [begin:end]         Los elementos desde 'begin' sin incluir 'end'
    [begin:]            Todos los elementos desde 'begin' hasta el final de la lista
    [:end]              Todos los elementos hasta 'end' sin incluirlo
    [:]                 Todos los elementos de la lista
    [begin:end:step]

    Las lista son mutables (se pueden modificar), se puede utilizar 'slicing'
    para especificar tanto un objetivo como una fuente de una asignación!

"""

print('Indexado ', str(fahr_list[0]), ' Tamaño de la lista: ', len(fahr_list))

lista_enteros = [1, 2, 5, 7]
lista_enteros[:2] = [10, 20, 30, 40]
# Si se intenta reemplazar un elemento sin utilizar 'slicing',
# el efecto resultante es que estaríamos colocando una lista dentro de otra
lista_enteros[0] = [-70, -60]
# Inserta elementos en la posición indicada y desplaza los demás elementos :P
lista_enteros[3:3] = [-3, -2, -1]
print(lista_enteros)

"""

    Python proporciona una manera sencilla de trabajar secuencias de enteros,
    para ello se utiliza la función integrada 'range'
    Cabe señalar que los rangos son muy útiles para iterar sobre listas ...
    La formas de utilizar la función son las siguientes:
    ~ si se omite el inicio se infiere que el índice comienza en cero
    range(end), range(start, end), range(start, end, step)
    Importante señalar que el último índice es omitido (end)!!

"""

temp_list = [0.01, 67.3, 21.2, 15.1]
contador = "Niemand"
for contador in range(len(temp_list)):
    temp_list[contador] = temp_list[contador] * 1.8 + 32.0

print(temp_list)

"""

    Una forma de eficientar el código Python es no utilizar tanto 'print'
    para ello se recomienda utilizar el método 'join' y al final
    imprimir la cadena resultante ...
    En el siguiente ejercicio se muestra su uso para hallar números primos :)

"""

bool_list = [True] * 100
primes_found_list = []

for prime in range(2, 100):
    if bool_list[prime]:
        primes_found_list.append(str(prime))
        for i in range(prime * prime, 100, prime):
            bool_list[i] = False
out_str = ' '.join(primes_found_list)
print(out_str)

# Algunas funciones de útilidad en listas son 'len', 'min' y 'max'
# Las palabras clave 'in' y 'not in' igual permiten hacer búsquedas rápidas

my_list = [300, 400, 50]
print(300 in my_list)
print(50 not in my_list)

"""

    Python 2.0 introduce la función 'enumerate' la cual nos permite
    iterar directamente sobre la información mientras se obtiene un índice "for free"
    Genera una serie de tuplas en la forma (index, item). Su sintaxis es la sig:

    enumerate(iterable, start=0)

"""

beat_list = ['John', 'Paul', 'George', 'Ringo']
for index, beat_str in enumerate(beat_list, 1) :
    print(index, '. ', beat_str, sep='')

# Compresión de listas Python
lista_pares = [entero * 2 for entero in range(10)]
lista_numeros = [i * j for i in range(1, 4) for j in range(1, 4) if i >= j]
print(lista_numeros)

"""

    Las estructuras de datos 'set' en Python tienen ciertas caracteristicas:
    - Un elemento de un set debe ser único, debe aparecer una sóla vez en el conjunto
      (una lista puede tener cualquier número de valores duplicados)
    - El order de los elementos no importa {1, 2, 3} = {3, 2, 1}
      (en las listas el orden sí importa de hecho)

    Python soporta capacidades de indexado y 'slicing' en cadenas sin problema.
    El método 'split' permite separar una cadena en componentes ...
    Para concatenar cadenas se utiliza el símbolo de adición (+)
    Mientras que para conformar cadenas es útil el método 'join'

"""

# Solamente se agregarán en el set los elementos únicos, los repetidos se ignoran ...
python_set = { 2, 4, 5, 5, 5, 6, 5, 7, 6 }
print(python_set)

print("Niemand verascht Dionisos"[:-8])
print("Niemand verascht Dionisos"[17:] + " Kaiser!")

cadena = 'A man, a plan, a canal, Panama!'
print(cadena.split(','))

artist_list = ['John', 'Paul', 'George', 'Ringo']
separador = "-"
print(separador.join(artist_list))

"""
Python Without Fear - Brian Overland
Ed. Addison-Wesley Professional 2017
SECUENCIA
python_functions.py
"""
