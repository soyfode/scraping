import json
import pandas as pd

# open data
f = open('../data/laNacion.json')
data = json.load(f)
# Crear un dataframe con los datos
df = pd.DataFrame(data)

#Eliminar los primeros 4 caracteres de la fecha
df['fecha'] = df['fecha'].str[4:]

# reemplazar mes del año por numero loop
meses = {'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04', 'may': '05', 'jun': '06', 'jul': '07', 'ago': '08', 'sept': '09', 'oct': '10', 'nov': '11', 'dic': '12'}
for key, value in meses.items():
    df['fecha'] = df['fecha'].str.replace(key, value)

#Reemplazar punto y como por dos puntos
df['titular'] = df['titular'].str.replace(';', ':')

# borrar coma 
df['fecha'] = df['fecha'].str.replace(',', '')

# borrar espacio en blanco del principio
df['fecha'] = df['fecha'].str.strip()

# transformar columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d %m %Y')

# exportar df a csv
df.to_csv('../data/paginaSiete.csv', index=False)

# exportar df['titular'] y df['fecha'] a csv
df[['titular', 'fecha']].to_csv('../data/laNacion.csv', index=False)
