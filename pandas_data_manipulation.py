
"""
    Una de las formas más sencillas de combinar información es mediante
    la técnica de 'concatenación', la cual puede pensarse como el agregar
    una fila o también una columna a nuestra información.
    Para lograr lo anterior se utiliza la función concat() y si se requiere
    solamente agregar un objeto simple a un DataFrame se utiliza append()
"""

import pandas as pd
import numpy

df1 = pd.read_csv('../../Pandas Data/concat_1.csv')
df2 = pd.read_csv('../../Pandas Data/concat_2.csv')
df3 = pd.read_csv('../../Pandas Data/concat_3.csv')

# Los tres DataFrame concatenados tienen la misma estructura ...
# Si no se ignoran los índices se muestran entonces duplicados :S
# print(pd.concat([df1, df2, df3], ignore_index=True))

new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
# Si concatenamos una serie equivale a agregar una nueva columna ...
# Todos los elementos que no puedan ser mapeados se mostrarán como un NaN
# print(pd.concat([df1, new_row_series]))

new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])
# Claro también es posible crear la estructura de un DataFrame para concatenarla
# print(pd.concat([df1, new_row_df]))

data_dict = {'A': 'n1', 'B': 'n2', 'C': 'n3', 'D': 'n4'}
# Los diccionarios pueden utilizarse para complementar un DataFrame
# Es importante notar que las llaves del diccionario coinciden con las columnas!
#print(df1.append(data_dict, ignore_index=True))

# Concatenar columnas es muy similar a concatenar registros
# La diferencia radica en el parámetro axis (default 0 para filas/registros)
# Para evitar nombres de columnas duplicados se resetea el index ~
col_concat = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
# Agregar una columna a un DataFrame puede hacerse directamente ...
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])

"""
    Pandas también permite concatenar aún y cuando los índices de fila/columna
    no están alineados (las dimensiones entre estructuras son diferentes)
    Una forma de evitar la inclusión de valores NaN al concatenar, es mantener
    sólo aquellas columnas que son comunes mediante el parámetro 'join'
    ~ mediante 'inner' se mantienen sólo los campos en común
"""

df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

# Se utiliza 'sort' en falso debido a que los DataFrame no están "alineados"
row_concat = pd.concat([df1, df2, df3], sort=False)
#print(pd.concat([df1, df3], sort=False, join='inner'))

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

col_concat = pd.concat([df1, df2, df3], axis=1)
#print(pd.concat([df1, df3], axis=1, join='inner'))


"""
    A veces es necesario combinar dos o más DataFrames basándonos en
    valores de datos comunes, tal y como un join en base de datos ...
    Para ello se utiliza la función 'merge' del DataFrame
    Si Pandas encuentra colisiones en los nombres de las columnas,
    agrega sufijos para los valores del 'left dataframe' (_x) y también
    para el 'right dataframe' (_y)
"""

person = pd.read_csv('../../Pandas Data/survey_person.csv')
site = pd.read_csv('../../Pandas Data/survey_site.csv')
survey = pd.read_csv('../../Pandas Data/survey_survey.csv')
visited = pd.read_csv('../../Pandas Data/survey_visited.csv')

visited_subset = visited.loc[[0, 2, 6], ]

one_to_one_merge = site.merge(visited_subset, left_on='name', right_on='site')
many_to_one_merge = site.merge(visited, left_on='name', right_on='site')

# Relación 'many to many' en DataFrames
ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')
person_visited = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'], right_on=['person', 'ident', 'quant', 'reading'])
# print(person_visited)

"""
    La información perdida en Pandas se representa como un NaN,
    dicho valor especial no es equiparable con ningún otro valor
    incluso NaN == NaN retorna falso!
    Pandas tiene métodos para poder checar la existencia de tal valor ...

    print(pd.isnull(NaN))
    print(pd.notnull(NaN))

    La función read_csv tiene tres parámetros relacionados con los NaN
    na_values permite especificar los valores a reconocer como NaN
    keep_default_na booleano para permitir utilizar solamente 'na_values'
    na_filter booleano para cargar todo ignorando NaN

    El usuario también puede crear valores perdidos ...
"""

visited_file = '../../Pandas Data/survey_visited.csv'
# print(pd.read_csv(visited_file, na_values=[''], keep_default_na=False))
num_legs = pd.Series({'goat': 4, 'amoeba': numpy.nan})

gapminder = pd.read_csv('../../Pandas Data/gapminder.tsv', sep='\t')
life_exp = gapminder.groupby(['year'])['lifeExp'].mean()

# Si falta información en una Serie se puede usar Re-indexing ...
year2000 = life_exp[life_exp.index > 2000]
# print(year2000.reindex(range(2000, 2010)))

ebola = pd.read_csv('../../Pandas Data/country_timeseries.csv')
num_registros = ebola.shape[0]
num_perdidos = num_registros - ebola.count()
# print(num_perdidos)

# El método 'fillna' permite reemplazar los NaN por un valor específico,
# incluso cuenta con el parámetro 'inplace' para afectar directamente
# el DataFrame sin necesidad de crear una copia
# También se puede rellenar con el valor conocido anterior o siguentes,
# siempre y cuando exista un valor de referencia en caso contrario sigue NaN

# print(ebola.fillna(0).iloc[0:10, 0:5])
# print(ebola.fillna(method='ffill').iloc[0:10, 0:5])
# print(ebola.fillna(method='bfill').iloc[:, 0:5].tail())

# Se puede usar interpolación para rellenar valores perdidos ...
# Aunque claro la aproximación no sigue una lógica compleja
# print(ebola.interpolate().iloc[0:10, 0:5])

# Si hay pocos valores perdidos tal vez sea bueno eliminar dichos
# registros para nuestro análisis, se realiza mediante 'dropna'
# print(ebola.dropna())

# Es posible realizar operaciones entre columnas pero sólo funciona
# cuando no existen valores NaN, lo cual invalida la operación!
# Métodos de Pandas ignoran los NaN por default, tal como la suma, media, etc.
ebola['Cases_multiple'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n=10))
print(ebola.Cases_Guinea.sum(skipna = True))

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
SECUENCIA
pandas_tidy_data.py
"""
