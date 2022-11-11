import json
import pandas as pd

# open data
f = open('../data/paginaSiete_v2.json')
data = json.load(f)

# Crear un dataframe con los datos
df = pd.DataFrame(data)
# Eliminar corchete
df['titulo'] = df['titulo'].str[0]
df['fecha'] = df['fecha'].str[0]
df['hora'] = df['hora'].str[0]

# transformar columna 'hora' a datetime hora y minutos sin fecha
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M').dt.time

# reemplazar mes del año por numero loop
meses = {'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04', 'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08', 'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'}
for key, value in meses.items():
    df['fecha'] = df['fecha'].str.replace(key, value)

# remover la la palabra 'de' de la columna 'fecha'
df['fecha'] = df['fecha'].str.replace('de', '')

#Reemplazar punto y como por dos puntos
df['titulo'] = df['titulo'].str.replace(';', ':')

# transformar columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%d %m %Y')

# exportar df a csv
df.to_csv('../data/paginaSiete.csv', index=False)

# exportar df['titulo'] a csv
df['titulo'].to_csv('../data/paginaSiete_titulo.csv', index=False)
