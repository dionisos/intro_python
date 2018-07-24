
"""

	Para los ejemplos que se mostrarán a continuación se utiliza un conjunto de información
	diseñada por el estadista 'Frank Anscombe' para mostrar la importancia de las gráficas ...
	La información se conforma por cuatro conjuntos, cada uno maneja dos variables continuas.
	Cada conjunto tiene la misma media, varianza, correlación y regresión lineal.
	Sin embargo, sólo cuando la información es visualizada resulta obvio que los conjuntos
	no siguen el mismo patrón, lo cual demuestra el beneficio de su visualización!

	~ la información se encuentra dentro de la librería 'seaborn'
	pip install seaborn

"""

import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")
tips = sns.load_dataset("tips")


# PLOT LINE
"""
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

fig.suptitle("Anscombe Data")
fig.tight_layout()
"""


# HISTOGRAM
"""
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')
"""


# SCATTER
"""
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
"""


# BOXPLOT
# Se utiliza cuando una variable discreta es graficada contra una variable continua
# El primer argumento de 'boxplot' es la información a graficar (lista si son varios rubros)
"""
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot(
    [tips[tips['sex'] == 'Female']['tip'], tips[tips['sex'] == 'Male']['tip']],
    labels=['Female', 'Male'])

axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')
"""


# SCATTER
"""
def recode_sex(sex) :
	if sex == 'Female' :
		return 0
	else :
		return 1

tips['sex_color'] = tips['sex'].apply(recode_sex)
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(x=tips['total_bill'], y=tips['tip'], s=tips['size'] * 10, c=tips['sex_color'], alpha=0.5)
axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
"""


##########################################
# LIBRERÍA 'SEABORN'
##########################################

# HISTOGRAM
"""
# La librería 'matplotlib' proporciona la funcionalidad básica de ploteo en Python,
# mientras que 'seaborn' está construída sobre la misma para proporcionar
# caracteristicas más avanzadas y gráficas más complejas ...

hist, ax = plt.subplots()
# Se puede mostrar una gráfica de densidad - Kernel Density Estimation (KDE)
# Las gráficas 'Rug' son representaciones de una variable de distribución en una dimensión!
ax = sns.distplot(tips['total_bill'], kde=True, rug=True)
ax.set_title('Total Bill Histogram with Density Plot')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')
"""


# COUNT PLOT (BAR PLOT)
"""
# Similar a un histograma, pero en lugar de utilizar 'binning values' para producir una
# distribución, se pueden emplear barras para contar valores discretos

ax = plt.subplots()
ax = sns.countplot('day', data=tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
"""


# SCATTERPLOT
"""
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
"""


# JOINPLOT
"""
# Se puede agregar una gráfica univariable en cada eje con 'joinplot'
joint = sns.jointplot(x='total_bill', y='tip', data=tips)
joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
"""


# HEXBINPLOT
"""
# Si son demasiados puntos para mostrar en un scatterplot se recomienda un 'HexbinPlot'
hexbin = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
"""


# KDEPLOT (Kernel Density Estimation)
"""
kde, ax = plt.subplots()
ax = sns.kdeplot(data=tips['total_bill'], data2=tips['tip'], shade=True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
kde_joint = sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
"""


# PAIRPLOT
"""
fig = sns.pairplot(tips, hue='sex')
pair_grid = sns.PairGrid(tips)
# we can use plt.scatter instead of sns.regplot
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
"""


##################################
# PANDA OBJECTS
##################################

# Los objetos Panda vienen equipados con sus propias funciones de ploteo, basadas en matplotlib con valores predefinidos ...
# en general las funciones de ploteo están dadas en la forma DataFrame.plot.PLOT_TYPE y Series.plot.PLOT_TYPE

fig, ax = plt.subplots()
# ax = tips['total_bill'].plot.hist() # Gráfica de un Series
# ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax) # Gráfica de un DataFrame
# ax = tips['tip'].plot.kde()
# ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax)
#ax = tips.plot.hexbin(x='total_bill', y='tip', gridsize=10, ax=ax)
ax = tips.plot.box(ax=ax)
plt.show()


"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
SECUENCIA
pandas_data_manipulation.py
"""
