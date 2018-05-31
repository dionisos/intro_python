
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
print(type(subset_loc)) # class 'pandas.core.series.Series'
# Seleccionar los registros 1er. 100th, 1000th
#print(df.loc[[0, 99, 999]])
#print(df.iloc[[-1, 0]])

# Recordar que iloc() solamente funciona con índices no con identificadores!
subset_loc = df.loc[[0], ['country','continent','year']]
print(df.iloc[[17], :])

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
print(flat.head(8))

# Para saber la cantidad de valores únicos y frecuencias en una Serie de Pandas:
# print(df.groupby('continent')['country'].nunique())
# print(df.groupby('continent')['country'].value_counts())


"""
PENDIENTE
Pandas for Everyone: Python Data Analysis
2. Pandas Data Structures
"""
