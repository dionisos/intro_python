
import pandas as pd
import seaborn as sns
import numpy as np

"""
    El tipo de dato que almacena una columna gobierna que tipo de funciones
    y cálculos pueden realizar con los datos de la misma.
    Es por ello que una conversión adecuada entre tipos suele ser importante.
    Para convertir una columna se usa su método Series.astype(), que toma como
    argumento cualquier 'dtype' de la librería numpy (str, float, int, category, etc.)

    La función de Pandas to_numeric() permite un mejor manejo de cast
    hacia valores númericos, pudiendo incluso indicar valores en caso de error
    raise - (default) lanza un error y termina la conversión
    coerce - NaN si no se puede convertir a valor numérico
    ignore - retorna el valor que no se pudo convertir
"""

tips = sns.load_dataset("tips")
tips['sex_str'] = tips['sex'].astype(str)

tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce')
print(tips_sub_miss.head())


"""
    Una cadena de texto puede verse como un contenedor de caracteres
    en donde el primer índice inicia con 0 (Zero) y al revés con -1
    ~ es posible realizar slicing sobre los caracteres
    Al realizar slicing en cadenas también es posible indicar un incremento,
    el cual indicará cada cuántos caracteres se tomarán caracteres ...
"""

word = 'grail'
sent = 'a scratch'
s_len = len(sent)

print("~ MANEJO DE CADENAS ")
# print(word[0:3])
# print(sent[2:s_len])
# print(sent[::2])

# print("black Knight".capitalize())
# print("Niemand verascht Carlos!".count("a"))
# print("coconut".endswith('nut'))
print("Scratch".upper())
print("flesh wound".replace('wound', 'for fantasy'))
print("Aprendiendo Pandas Python".split(sep=' '))

d1 = '40°'
m1 = "46'"
s1 = '52.837"'
u1 = 'N'
d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'

print(' '.join([d1, m1, s1, u1, d2, m2, s2, u2]))

cadena = """Black Knight: 'Tis but a {0}.
King Arthur: A {0}? Your arm's off!"""

print(cadena.format('scratch'))
cadena = 'Hayden Planetarium Coordinates: {lat}, {lon}'
print(cadena.format(lat='40.7815° N', lon='73.9733° W'))
print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
print('Some digits of %(cont)s: %(value).2f' % {'cont': 'e', 'value': 2.718})

"""
    Para aplicar una función a través de cada fila o columna de un DataFrame
    se utiliza un 'apply' el cual es más eficiente que utilizar un loop for p.e.
    La estructura Series tiene el método apply(), en el cual podemos pasar
    la función que vamos a "aplicar a través de cada elemento" en la serie
    DataFrame también permite utilizar 'apply' la única diferencia es que
    debemos indicar si aplicará en las columnas (axis=0) o en filas (axis=1)
"""

def my_sq(x) :
    return x ** 2

df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})
cuadrado = df['a'].apply(my_sq) # pandas.core.series.Series

# Equivalente a lo anterior ...
# print(df['a'] ** 2)
# No obstante para cosas más complejas sin duda no hay más que 'apply'

def my_exp(x, e) :
    return x ** e
exponente = df['a'].apply(my_exp, e = 2.17)

def avg_3_apply(col) :
     return (col[0] + col[1] + col[2]) / 3
promedio_columna = df.apply(avg_3_apply)

def avg_2_apply(row) :
   return (row[0] + row[1]) / 2
promedio_fila = df.apply(avg_2_apply, axis=0)


def count_missing(vec) :
    null_vec = pd.isnull(vec) # vector de valores True/False
    null_count = np.sum(null_vec) # valores null no contribuyen a la suma
    return null_count

def prop_missing(vec) :
    return count_missing(vec) / vec.size

def prop_complete(vec) :
    return 1 - prop_missing(vec)

titanic = sns.load_dataset("titanic")

# Los siguientes estadísticos nos sirven para ver que columnas pueden
# utilizarse dentro de un estudio ... aquellas sin tantos missing :P
cmis_col = titanic.apply(count_missing)
pmis_col = titanic.apply(prop_missing)
pcom_col = titanic.apply(prop_complete)

# sólo hay dos registros faltantes en la columna  embark_town
print(titanic.loc[pd.isnull(titanic.embark_town), :])

titanic['num_missing'] = titanic.apply(count_missing, axis=1)
print(titanic.loc[titanic.num_missing > 1, :].sample(10))

"""
    Para tomar ventaja de las bondades de numpy y sus operaciones vectorizadas
    podemos implementar las funciones a modo de que la lógica a ejecutar
    represente la manipulación de vectores y no elementos individuales,
    lo cual dará mayor rapidez a los cálculos.
    Para ello debemos emplear un 'decorador' antes de la definición
    de la función misma, el elemento @np.vectorize
"""

@np.vectorize
def v_avg_2_mod(x, y) :
    if (x == 20) :
        return(np.NaN)
    else :
        return (x + y) / 2

print("~ VECTORIZACIÓN DE FUNCIONES")
print(v_avg_2_mod(df['a'], df['b']))

# Algunas veces la función utilizada en el método 'apply' es tan simple
# que no es necesario crear una función separada; en su lugar se utiliza
# un 'lambda' escribiendo la función directamente sin tener que definirla,
# el resultado calculado es automáticamente regresado.
# Típicamente se utilizan los lambda solamente con cálculos de una línea ..

import regex

patron = regex.compile('\w+\s+\w+')
def get_name(cadena) :
     return patron.match(cadena).group()

docs = pd.read_csv('../../Pandas Data/doctors.csv', header=None)
docs['name_func'] = docs[0].apply(get_name)
docs['name_lamb'] = docs[0].apply(lambda cadena: patron.match(cadena).group())
print(docs)


"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
8.6 Regular Expressions (REGEX)
SECUENCIA
pandas_groupby_operations.py
"""
