
"""
    Tidy Data es un framework para estructurar conjuntos de información
    a modo de que puedan ser analizados y visualizados fácilmente.
    Existen ciertos criterios que debe cumplir un "tidy data"
    - Cada fila es una observación
    - Cada columna es una variable
    - Cada tipo de unidad de observación forma una tabla

    Cuando existe un data set en donde cada columna no es una variable
    (se utiliza normalmente cuando se presenta información en forma de tabla)
    es necesario realizar un "unpivot/melt/gather" a nuestro DataFrame.
    Pandas cuenta con una función llamada melt() la cual redimensiona
    un DataFrame en un formato tidy utilizando ciertos parámetros:

    id_vars - Lista, tupla, ndarray que representa las variables a mantener
    value_vars - Las columnas a fundir (unpivot), default todas menos id_vars
    var_name - Nombre cuando value_vars es fundido (default 'variable')
    value_name - Nombre que representa los valores de var_name (default 'value')
"""

import pandas as pd

# Columnas contienen valores y no variables ...
pew = pd.read_csv('../../Pandas Data/pew.csv')
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
# print(pew.iloc[0:5, 0:6])
# print(pew_long.head())

# Fundir columnas (melt) pero manteniendo varias columnas fijas ...
billboard = pd.read_csv('../../Pandas Data/billboard.csv')
billboard_long = pd.melt(
    billboard,
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating')

# print(billboard.iloc[0:5, 0:16])
# print(billboard_long.head())

# El método melt() aplica aun y cuando columnas representan múltiples variables!
ebola = pd.read_csv('../../Pandas Data/country_timeseries.csv')
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
# print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])
# print(ebola_long.head())

"""
  En el ejemplo anterior dentro de 'variable' tenemos dos conceptos
  que podemos separar a su vez como nuevas variables (unidas por un guión bajo)
  Para ello hay que acceder a la columna variable generada previamente ...
  A continuación varios métodos de lograrlo!
"""

# PRIMER MÉTODO
# variable_split = ebola_long.variable.str.split('_')
# status_values = variable_split.str.get(0)
# country_values = variable_split.str.get(1)
# print(type(variable_split)) # pandas.core.series.Series
# print(type(variable_split[0])) # class 'list'
# ebola_long['status'] = status_values
# ebola_long['country'] = country_values
# print(ebola_long.head())

# MÉTODO ALTERNATIVO ~ CONCATENANDO
# variable_split = ebola_long.variable.str.split('_', expand=True)
# variable_split.columns = ['status', 'country']
# ebola_parsed = pd.concat([ebola_long, variable_split], axis=1)
# print(ebola_parsed.head())

# MÉTODO COMPLICADO
# zip() toma una conjunto de iteradores y crea un contenedor asociado uno a uno
# En Python se utiliza un asterisco (*) para a su vez desempacar contenedores
ebola_long['status'], ebola_long['country'] = zip(*ebola_long.variable.str.split('_'))
# print(ebola_long.head())


"""
    A veces ocurre que los datos están formateados de modo que hay variables
    tanto en filas como en columnas. Siendo que una columna puede mantener
    varias variables en este caso debemos "pivotear" en columnas separadas ...
    pivot_table() es un método del objeto DataFrame ~
"""

weather = pd.read_csv('../../Pandas Data/weather.csv')
weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
weather_tidy = weather_melt.pivot_table(index=['id', 'year', 'month', 'day'], columns='element', values='temp').reset_index()
# Importante checar las dos transformaciones que sufre el DataFrame
# print(weather.iloc[:5, :11])
# print(weather_melt.head())
# print(weather_tidy.head())


# NORMALIZACIÓN
# Tal y como en el Modelo Entidad-Relación para evitar redundancia ...
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
billboard_songs = billboard_songs.drop_duplicates()
billboard_songs['id'] = range(len(billboard_songs))
billboard_ratings = billboard_long.merge(billboard_songs, on=['year', 'artist', 'track', 'time'])
billboard_ratings = billboard_ratings[['id', 'date.entered', 'week', 'rating']]
# print(billboard_long.head())
# print(billboard_songs.head())
# print(billboard_ratings.head())

# Cargar múltiples fuentes de datos y ensamblarlas!
import os
import urllib
import glob

"""
# Descargar los archivos del repositorio en línea ...
with open('../../Pandas Data/raw_data_urls.txt', 'r') as data_urls:
    for line, url in enumerate(data_urls):
        if line == 3:
            break
        fn = url.split('/')[-1].strip()
        fp = os.path.join('.', 'archivos', fn)
        print(fp + " <- " + url, end='')
        urllib.request.urlretrieve(url, fp)
"""

nyc_taxi_data = glob.glob('./archivos/fhv_*')
list_taxi_df = []

"""
for csv_filename in nyc_taxi_data :
    df = pd.read_csv(csv_filename)
    list_taxi_df.append(df)
"""

# Método "List Comprehension" equivalente al loop anterior
list_taxi_df = [pd.read_csv(data) for data in nyc_taxi_data]
taxi_loop_concat = pd.concat(list_taxi_df)

print(nyc_taxi_data)
print("Registros concatenados: ", taxi_loop_concat.shape)

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
SECUENCIA
pandas_data_types.py
"""
