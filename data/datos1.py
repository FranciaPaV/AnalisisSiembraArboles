import pandas as pd

#obtenemos los datos de la DB
tabla = pd.read_csv('./data/Siembras.csv')
print(tabla)