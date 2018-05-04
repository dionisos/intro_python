
"""
    En Python no se pueden pasar parámetros por referencia como en C/C++
    Es posible retornar de una función más de un valor ...

    Podemos hacer referencia a los argumentos de un método por nombre!
    con lo cual no importa el orden en que pasemos los argumentos,
    la única restricción es que los parámetros sin nombre se toman en orden :P
    ~ es una caracteristica interesante que no he visto en otro lenguaje

    Es posible también indicar argumentos por default en un método,
    la única condición es que deben colocarse al final de las definiciones.
    Durante el llamado a una función, un argumento puede omitirse si es default :)

    Para indicar explícitamente que no se retorna un valor se puede usar 'None'
    Hay tres distintas técnicas para importar funciones de módulos en Python,
    la diferencia radica en si se cualifican con el nombre del módulo o no ¬¬
"""

def calc_pts(x1, y1, x2, y2) :

    dist1 = y2 - y1
    dist2 = x2 - x1
    dist = (dist1 ** 2 + dist2 ** 2) ** 0.5
    sum = [x1 + x2, y1 + y2]

    return dist, sum


def funcion_exponente(a, b, e) :
    return a * (b**e)

print("Distintas configuraciones: ", end='')
print(funcion_exponente(1, 2, 5), end=', ')
print(funcion_exponente(1, e=5, b=2), end=', ')
print(funcion_exponente(b=2, e=5, a=1))

def repeat_string(a_str, n = 1, e = 1) :
    for i in range(n) :
        print(a_str)
    return None

repeat_string('Nabucodonosor!', e = 3)

import random
from numbers import Real
from fractions import *

aleatorio = random.randint(0, 9)

"""
    Una variable global tiene el mismo tiempo de vida que el programa y
    puede ser vista y utilizada por múltiples funciones.
    Éste tipo de variables son creadas mediante la palabra clave 'global' ó
    también definiendo variables fuera de una función "a nivel de módulo"
    Al usar 'global' Python busca una variable con el nombre indicado,
    si ya existe se utiliza dicha versión, si no es así se crea una nueva ...
    (no crea directamente una variable, previene que se interprete como local)
"""

def resent_funds() :
    global n_bank_acct
    n_bank_acct = 10500

resent_funds()
print("Variable global:", n_bank_acct)

# Función para crear números romanos ...
# Apoyándose de la variable global 'amt' en la construcción del algoritmo :P

rom_list = [ ('M', 1000), ('CM', 900), ('D', 500),
             ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
             ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1) ]

amt = int(input('Entero para convertir a Romano: '))
print('El número romano es: ', end='')

def make_roman(letter, n) :
    global amt
    while amt >= n :
        amt = amt - n
        print(letter, end='')

for item in rom_list:
    make_roman(item[0], item[1])

def decode_roman(letters, n) :
    global entero_equivalente, romstr
    sz = len(letters)
    while len(romstr) >= sz and letters == romstr[:sz] :
        entero_equivalente += n
        romstr = romstr[sz:]

entero_equivalente = 0
romstr = input('\nNúmero Romano para convertir a entero: ')
for item in rom_list :
    decode_roman(item[0], item[1])
print('El número equivalente es:', entero_equivalente)

"""
    Python proporciona el módulo 'os' para interactuar con archivos y directorios
    Existen varios métodos de utilidad para gestionar recursos en disco:

    listdir()   - lista el contenido del directorio actual
    chdir()     - cambia el directorio actual de trabajo
    getcwd()    - full path del directorio de trabajo

    Si se abre un archivo para escritura y no existe, uno nuevo es creado.
    Pero si existe, el contenido anterior es borrado y reemplazado por el nuevo :P
"""

import os
file_list = os.listdir()
for item in file_list :
    print(item)

os.chdir('archivos')
file_object = open('dionisos.txt', 'w')
file_object.write('Exploración FC\n')
file_object.close()

"""
PENDIENTE
11. Write File with Prompt ...
"""
