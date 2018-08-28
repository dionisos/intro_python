
"""
    Las operaciones de agrupamiento son una poderosa forma de conjuntar,
    transformar y filtrar datos. Y aunque pueden realizarse mediante otras
    técnicas cuando empleamos sentencias 'groupby' el código es más rápido!
    Dichas operaciones se pueden ver como un "split-apply-combine"

    1. La información es separada en partes en base a una llave(s)
    2. Una función es aplicada a cada parte de la información
    3. Los resultados de cada parte se combinan para crear un nuevo data set

    'Agregación' es el proceso de tomar múltiples valores y retornar uno solo
    p.e. en los siguientes ejemplos, el calcular la expectativa de vida promedio
    por cada año es un caso de este tipo de operación 'groupby' ...
    Existen varios métodos de agregación en Pandas tales como:
    count, size, mean, std, describe, max, min, quantile(q=0.25), sum, var

    También es posible utilizar funciones de agregación de 'numpy', en lugar de
    llamarlas directamente se pasan a las funciones 'agg' y 'aggregate'
    Del mismo modo, podemos pasar nuestras propias funciones sin problema!
"""

import pandas as pd
import numpy as np

df = pd.read_csv('../../Pandas Data/gapminder.tsv', sep='\t')
# avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
# print(avg_life_exp_by_year)

# print(df.loc[df.year == 1952, :].lifeExp.describe())
continent_describe = df.groupby('continent').lifeExp.describe()
print(continent_describe)

def my_mean(values) :
    n = len(values)
    sum = 0
    # iterar sobre los valores de panda.Series
    for value in values :
        sum += value
    return(sum / n)

def my_mean_diff(values, diff_value) :
    n = len(values)
    sum = 0
    for value in values :
        sum += value
    mean = sum / n
    return(mean - diff_value)

cont_le_agg = df.groupby('continent').lifeExp.agg(np.mean)
cont_le_aggregate = df.groupby('continent').lifeExp.aggregate(np.mean)
agg_my_mean = df.groupby('year').lifeExp.agg(my_mean)

global_mean = df.lifeExp.mean()
agg_mean_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value=global_mean)
# print(agg_mean_diff)

"""
    Es posible pasar varias funciones a los métodos 'agg' y 'aggregate'
    Por otro lado, también podemos utilizar un diccionario para aplicar
    funciones en los métodos 'agg' y 'aggregate', si se aplica en un DataFrame
    las llaves son las columnas y los valores las funciones a aplicar!
    ~ lo anterior permite agrupar una o más variables y funciones de una vez
    Si se aplica a una Series es necesario renombrar las columnas resultantes
"""

functions_df = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
# print(functions_df)

# Funciones aplicadas a columnas de un pandas.DataFrame
dataframe_gdf_dict = df.groupby('year').agg({
    'lifeExp': 'mean',
    'pop': 'median',
    'gdpPercap': 'median'
})

# Diversas funciones aplicadas a una pandas.Series ~ renombrando columnas
series_gdf = df.groupby('year')['lifeExp'].\
    agg([np.count_nonzero, np.mean, np.std,]).\
    rename(columns={'count_nonzero': 'count', 'mean': 'avg', 'std': 'std_dev'}).\
    reset_index()

# print(dataframe_gdf_dict)
# print(series_gdf)


"""
    A diferencia de 'aggregate', que puede tomar múltiples valores y regresar
    un sólo valor, 'transform' toma múltiples valores y retorna una
    transformación uno a uno de los valores. Es decir, no reduce la información.
"""

# Por ejemplo calculando el z-core se identifica el número de desviaciones
# estándar de la media hacia nuestros datos. Dicha técnica estandariza
# nuestros datos y hace más sencillo comparar diferentes variables ...

def my_zscore(x) :
    return((x - x.mean()) / x.std())

from scipy.stats import zscore
sp_z_grouped = df.groupby('year').lifeExp.transform(zscore)
transform_z = df.groupby('year').lifeExp.transform(my_zscore)

# print(transform_z.head())
# print(sp_z_grouped.head())

import seaborn as sns
import numpy as np

np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN

def fill_na_mean(x) :
    avg = x.mean()
    return(x.fillna(avg))

total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
# En este ejemplo se están llenando los valores NaN con las media por género!
# Para cada grupo de los datos se está utilizando la función 'fill_na_mean'
# print(tips_10[['sex', 'total_bill', 'fill_total_bill']])


"""
    La última acción que podemos aplicar en un 'groupby' son los filtros
    (anteriormente vimos agregación y transformación)
    Los filtros nos permiten agrupar información pero aplicando una regla
    de los elementos que se deben considerar en el resultado.
"""

tips = sns.load_dataset('tips')
tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
# print(tips_filtered['size'].value_counts())

# Es posible guardar los agrupamientos sin aplicar operación alguna,
# resultado de ello es una estructura pandas.core.groupby.DataFrameGroupBy
# Esto puede ser útil para aplicar múltiples operaciones de agregación,
# transformación y filtrado sin tener que procesar 'groupby' de nuevo ...

tips_10 = sns.load_dataset('tips').sample(10, random_state = 42)
grouped = tips_10.groupby('sex')
print(grouped.groups)

# Es posible extraer un grupo mediante get_group() ya como DataFrame
female = grouped.get_group('Female')

# Un beneficio de guardar el objeto 'groupby' es que podemos
# iterar a través de los grupos individualmente ...
# En cada iteración se tiene acceso a una tupla con el nombre del grupo
# como primer elemento (tipo 'str') y el DataFrame como segundo

for sex_group in grouped :
    print('the first element is: {}'.format(sex_group[0]))
    print('the second element of type {} is:\n{}'.format(type(sex_group[1]), sex_group[1]))
    break

bill_sex_time = tips_10.groupby(['sex', 'time'], as_index=False)
group_avg_dataframe = bill_sex_time.mean()
print(group_avg_dataframe)


"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
10.6 Working with a multi-index
~ no es posible cargar el archivo completo .csv
SECUENCIA
pandas_datetime_type.py
"""
