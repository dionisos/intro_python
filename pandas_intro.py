
"""

    Para instalar paquetes en Python una opción es utilizar 'pip' (package manager)
    Con dicha herramienta es posible gestionar paquetes fácilmente p.e. pandas ...
    En este caso para disponer del paquete que deseamos hay que ejecutar la sentencia:

    pip install pandas

    Pandas es una librería para análisis de datos. Le da la habilidad a Python de trabajar
    con información del tipo "spreadsheet" para su rápida carga, manipulación, alineación, etc.
    Introduce dos nuevos tipos de datos en el lenguaje: 'Series' y 'DataFrame'
    Hay una equivalencia entre los tipos de datos de Pandas y Python p.e.
    object-string, int64-int, float64-float, datetime64-datetime

    Para obtener registros de un DataFrame se pueden utilizar los métodos loc() e iloc()
    Cabe mencionar que el uso del método loc()/iloc() retorna el tipo 'Series'
    iloc() funciona exactamente igual, la diferencia radica en que podemos utilizar
    índices negativos (p.e. -1 es el último registro), algo que loc() no permite hacer
    ADEMÁS loc() FUNCIONA SOLAMENTE CON LOS NOMBRES DE COLUMNA :P
    Podemos con dichos métodos utilizar 'slicing' sin problemas:

    df.iloc/loc[[rows], [columns]]

    Cuando se desea hacer algún cálculo sobre un concepto de la información podemos
    emplear el método groupby() de DataFrame

"""

import pandas as pd
import random

# Mostrar los primeros registros del DataFrame para su inspección ...
df = pd.read_csv('../../Pandas Data/gapminder.tsv', sep='\t')
print(df.head(n = 1))

print(type(df)) # class 'pandas.core.frame.DataFrame'
print("Registros y columnas", df.shape)
print(df.columns)
#print(df.dtypes)
#print(df.info())

# Para examinar múltiples columnas se puede acceder a ellas mediante nombre, posición/rango
subset = df[['country', 'continent', 'year']]
#print(subset.tail())

number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
subset_loc = df.loc[last_row_index]
#print(type(subset_loc)) # class 'pandas.core.series.Series'
# Seleccionar los registros 1er. 100th, 1000th
#print(df.loc[[0, 99, 999]])
#print(df.iloc[[-1, 0]])

# Recordar que iloc() solamente funciona con índices no con identificadores!
subset_loc = df.loc[[0], ['country','continent','year']]
# print(df.iloc[[17], :])

small_range = list(range(3, 6))
subset = df.iloc[:, small_range]
# print(subset.head())
# Completamente equivalente a utilizar 'slicing' sin range()
# print(df.iloc[:, 3:6].head())

# Agrupar información del DataFrame para conjeturar datos ...
grouped_year_df = df.groupby('year') # pandas.core.groupby.groupby.DataFrameGroupBy
grouped_year_df_lifeExp = grouped_year_df['lifeExp'] # pandas.core.groupby.groupby.SeriesGroupBy
mean_lifeExp_by_year = grouped_year_df_lifeExp.mean() # pandas.core.series.Series
# print(mean_lifeExp_by_year)
# Equivalente a todo lo anterior! :P
# print(df.groupby('year')['lifeExp'].mean())

# Agrupar por más de un concepto y hacer el mismo cálculo en varias columnas!!
# ~ los cálculos de media en vida esperada e ingreso per capita se darán cada año en cada continente
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# print(multi_group_var)

# Si se desea mostrar el resultado sin "indentación" tipo Excel se usa reset_index()
flat = multi_group_var.reset_index()
# print(flat.head(8))

# Para saber la cantidad de valores únicos y frecuencias en una Serie de Pandas:
#print(df.groupby('continent')['country'].nunique())
#print(df.groupby('continent')['country'].value_counts())


"""

	El tipo de dato 'Series' es un contenedor de una dimensión (similar a una lista, con la
	diferencia de que todos sus elementos deben ser del mismo tipo),
	es el tipo que representa cada columna de un 'DataFrame'.
	El 'DataFrame' puede pensarse como un diccionario de objetos 'Series', en donde la llave
	es el nombre de la columna y los valores son del tipo 'Series'.

	La forma más sencilla de crear un tipo 'Series' es pasar una lista Python.
	Si se pasa una lista de tipos mezclados, el más común será utilizado (dtype)
	Para crear un 'DataFrame' se puede emplear una notación similar a un diccionario.
	Cabe mencionar que se pueden utilizar los parámetros 'columns' e 'index'

"""

estructura_series = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
#estructura_series = pd.Series(['apple', 'orange', 'lemon'])
#print(estructura_series)

scientists = pd.DataFrame\
({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]
})

from collections import OrderedDict

scientists = pd.DataFrame(
OrderedDict([
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']),
    ('Born', ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37, 61])
    ])
)

# Definición de 'scientists' similar pero con un orden establecido ...
# print(scientists)

# Indicamos el orden de las columnas y su índice (el nombre asociado)
scientists = pd.DataFrame\
(
    data={'Occupation': ['Chemist', 'Statistician'],
          'Born': ['1920-07-25', '1876-06-13'],
          'Died': ['1958-04-16', '1937-10-16'],
		  'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age']
)

# ~ en éste caso no será el índice un número entero, será el nombre!
# print(scientists)

"""

	La estructura Pandas 'Series' es muy similar a un numpy.ndarray (denominado "vector"),
	por lo cual muchos métodos y funciones aplican en ambos casos.
	~ cuando se tiene un vector de números, hay operaciones comunes que pueden realizarse
	min, max, mean, median, mode, quantile, hist, sort_values, describe, etc.
	Las operaciones entre series son alineadas y vectorizadas automáticamente (Broadcasting)

	Es posible alterar el tipo de dato de los elementos en un DataFrame (conversiones)
	p.e. cambiar el tipo cadena de texto (object) a un 'datetime' si es que cumple un formato

"""

# pandas.core.series.Series
first_row = scientists.loc['William Gosset']
#print(type(first_row))
#print(first_row.index)
#print(first_row.values)

ages = scientists['Age']
#print(ages)
#print(type(ages))

scientists = pd.read_csv('../../Pandas Data/scientists.csv')
ages = scientists['Age']
# print(ages.describe())
# Importante mencionar que podemos manejar subconjuntos de las series ...
subset_ages = ages[ages > ages.mean()]
rev_ages = ages.sort_index(ascending=False)

# Con los DataFrame es posible también manejar subconjuntos dada una restricción ...
first_half = scientists[:4]
subset_dataframe = scientists[scientists['Age'] > scientists['Age'].mean()]
# print(subset_dataframe)

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
# Es fácil agregar columnas a un DataFrame modificando otras ...
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
scientists['age_years_dt'] = scientists['age_days_dt'].astype('timedelta64[Y]')
#print(scientists.head())
#print(scientists.columns)

# Es posible crear un 'DataFrame' a partir de otro eliminando columnas ...
# Para hacer persistentes elementos Pandas se utiliza el formato "Pickle" en Python
# Si se requiere compartir la información con otras fuentes se puede utilizar CSV
# Para indicar el separador requerido o si los índices deben aparecer se usan 'sep' e 'index'
# Es posible almacenar y leer de formato Excel pero no es bien visto dentro de la
# "comunidad datascience" por varias cuestiones técnicas ... (checar paquetes xlwt, openpyxl)
scientists_dropped = scientists.drop(['Age'], axis = 1)
names = scientists['Name']
names.to_pickle('./archivos/scientists_names_series.pickle')
scientists.to_pickle('./archivos/scientists_df.pickle')

scientist_names_from_pickle = pd.read_pickle('./archivos/scientists_names_series.pickle')
scientists_from_pickle = pd.read_pickle('./archivos/scientists_df.pickle')
# print(scientist_names_from_pickle)

names.to_csv('./archivos/scientist_names_series.csv')
scientists.to_csv('./archivos/scientists_df.tsv', sep='\t')
scientists.to_csv('./archivos/scientists_df_no_index.csv', index=False)

scientists_from_csv = pd.read_csv('./archivos/scientists_df_no_index.csv', index_col=False)
#print(scientists_from_csv)

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
SECUENCIA
pandas_matplotlib_intro.py
"""
