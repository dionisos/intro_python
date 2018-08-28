
"""
    Convertir un objeto a un 'datetime' se realiza con la función 'to_datetime'
    Se pueden utilizar varias directivas para dar formato a las representaciones
    de tipo 'datetime' ... revisar tabla 11.1
    Es posible cargar automáticamente información y parsear los formatos de fecha:
    ebola = pd.read_csv('../../Pandas Data/country_timeseries.csv', parse_dates=[0])

    Disponiendo de una estructura tipo 'datetime' podemos extrar fácilmente
    sus componentes como atributos ~ year, month, day
"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

now = datetime.now()
time_unix = datetime(1970, 1, 1)
diferencia = now - time_unix

# Las operaciones entre tiempos genera instancias datetime.timedelta
print(type(diferencia))

ebola = pd.read_csv('../../Pandas Data/country_timeseries.csv')
# ebola['date_dt'] = pd.to_datetime(ebola['Date'])
ebola['date_dt'] = pd.to_datetime(ebola['Date'], format='%m/%d/%Y')

ebola['year'] = ebola['date_dt'].dt.year
ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month, ebola['date_dt'].dt.day)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())

# Una ventaja de manejar objetos de tiempo en un DataFrame es que
# se nos permite realizar cálculos con las fechas sin ningún problema ...
ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']].head())
# print(ebola.info())

banks = pd.read_csv('../../Pandas Data/banklist.csv', parse_dates=[5, 6])
banks['closing_quarter'], banks['closing_year'] = (banks['Closing Date'].dt.quarter, banks['Closing Date'].dt.year)
# print(banks.info())

closing_year = banks.groupby(['closing_year']).size()
closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()

"""
fig, ax = plt.subplots()
# ax = closing_year.plot()
ax = closing_year_q.plot()
plt.show()
"""

""" pip install pandas_datareader """
# import pandas_datareader as pdr
# tesla = pdr.get_data_yahoo('TSLA')

# Es posible sustraer información basándonos en objetos 'datetime'
tesla = pd.read_csv('../../Pandas Data/tesla_stock_yahoo.csv', parse_dates=[0])
print(tesla.loc[(tesla.Date.dt.year == 2010) & (tesla.Date.dt.month == 6)])


"""
    Cuando se trabaja con datos 'datetime' a veves es necesario establecer
    dicho objeto como el índice del DataFrame. Ahora, con el índice
    como un objeto 'datetime' podemos utilizarlo para seleccionar conjuntos!
    En forma similar podemos crear un objeto TimedeltaIndex para indexar
    el DataFrame y dividir por deltas de tiempo ...
"""

tesla.index = tesla['Date']
print(tesla['2010-06'].iloc[:, :5])

tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
tesla.index = tesla['ref_date']
# print(tesla.iloc[:5, :5])
print(tesla['0 day': '5 day'].iloc[:5, :5])

# Una práctica común es crear un rango de fechas para "reindexar" un data set
# Para dicho propósito se utiliza la función date_range() de Pandas
# ~ en realidad no entiendo muy bien lo de reindexar ... investigar!
head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5.reindex(head_range)
print(ebola_5.iloc[:, :5])

# La función date_range() permite definir la secuencia para generar
# los tiempos mediante el parámetro 'freq' ~ Revisar tabla 11.2
print(pd.date_range('2018-08-22', '2018-09-04', freq='B'))

# Dentro del parámetro 'freq' es posible crear offsets para la secuencia ..
# ~ p.e. cada dos días hábiles o el tercer viernes de cada mes
print(pd.date_range('2018-08-22', '2018-09-04', freq='2B'))
print(pd.date_range('2017-01-01', '2017-12-31', freq='WOM-3FRI'))

# En el ejemplo vamos a rellenar información faltante en la gráfica!
ebola = pd.read_csv('../../Pandas Data/country_timeseries.csv', index_col='Date', parse_dates=['Date'])

fig, ax = plt.subplots()
ax = ebola.plot(ax=ax)
ax.legend(fontsize=7, loc=2, borderaxespad=0.)
plt.show()

# RESAMPLING es una técnica para cambiar la frecuencia de un 'datetime'
down = ebola.resample('M').mean()
print(down.iloc[:5,:5])

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
~ Indagar en Pandas Datareader - descargar recursos en red
SECUENCIA
pandas_linear_models.py
"""
