
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

from sklearn import linear_model

"""
    Para realizar una regresión lineal se puede utilizar la librería 'statsmodels'
    Otra opción es la librería 'sklearn' ~ se muestran algunos ejemplos _
    Parece que 'statsmodels' es más amigable en primera instancia ...
"""

tips = sns.load_dataset('tips')
model = smf.ols(formula='tip ~ total_bill', data=tips)
results = model.fit()
# print(results.summary())
# print(results.params)

lr = linear_model.LinearRegression()
predicted = lr.fit(X=tips['total_bill'].values.reshape(-1, 1), y=tips['tip'])
# print(predicted.coef_)
# print(predicted.intercept_)

# REGRESIÓN MULTIPLE
model = smf.ols(formula='tip ~ total_bill + size', data=tips).fit()
print(model.summary())

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
12.3.2 Using statsmodels with Categorical Variables
"""
