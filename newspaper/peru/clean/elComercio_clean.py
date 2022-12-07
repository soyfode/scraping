import json
import pandas as pd

# open data
f = open('../data/prueba.json')
data = json.load(f)

# Crear un dataframe con los datos
df = pd.DataFrame(data)
# Eliminar corchete
df['titular'] = df['titular'].str[0]
df['fecha'] = df['fecha'].str[0]
df['hora'] = df['hora'].str[0]

# transformar columna 'hora' a datetime hora y minutos sin fecha
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M').dt.time


#Reemplazar punto y como por dos puntos
df['titular'] = df['titular'].str.replace(';', ':')

# transformar columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# exportar df a csv
df.to_csv('../data/paginaSiete.csv', index=False)

# exportar df['titulo'] a csv
df.to_csv('../data/elComercio1.csv', index=False)

2

f = open('../data/prueba2.json')
data = json.load(f)

# Crear un dataframe con los datos
df = pd.DataFrame(data)
# Eliminar corchete
df['titular'] = df['titular'].str[0]
df['fecha'] = df['fecha'].str[0]
df['hora'] = df['hora'].str[0]

# transformar columna 'hora' a datetime hora y minutos sin fecha
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M').dt.time


#Reemplazar punto y como por dos puntos
df['titular'] = df['titular'].str.replace(';', ':')

# transformar columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')

# exportar df a csv
df.to_csv('../data/paginaSiete.csv', index=False)

# exportar df['titulo'] a csv
df.to_csv('../data/elComercio2.csv', index=False)
