
import pandas as pd
import seaborn as sns

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
"""

word = 'grail'
sent = 'a scratch'
s_len = len(sent)

print(word[0:3])
print(sent[2:s_len])

"""
Pandas For Everyone: Python Data Analysis - Daniel Y. Chen
Ed. Addison-Wesley Professional 2017
PENDIENTE
8.2.2.1 Slicing From the Beginning to the End
"""
