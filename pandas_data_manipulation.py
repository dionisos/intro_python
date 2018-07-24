
"""
    Una de las formas más sencillas de combinar información es mediante
    la técnica de 'concatenación', la cual puede pensarse como el agregar
    una fila o también una columna a nuestra información.
    Para lograr lo anterior se utiliza la función concat() y si se requiere
    solamente agregar un objeto simple a un DataFrame se utiliza append()
"""

import pandas as pd

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
print(pd.concat([df1, df3], axis=1, join='inner'))


"""
    A veces es necesario combinar dos o más DataFrames basándonos en
    valores de datos comunes, tal y como un join en base de datos ...
    Para ello se utiliza la función 'merge' del DataFrame
"""

person = pd.read_csv('../../Pandas Data/survey_person.csv')
site = pd.read_csv('../../Pandas Data/survey_site.csv')
survey = pd.read_csv('../../Pandas Data/survey_survey.csv')
visited = pd.read_csv('../../Pandas Data/survey_visited.csv')

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
4.4 Merging Multiple Data Sets
"""
