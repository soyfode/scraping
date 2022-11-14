import pandas as pd
import numpy as np
import json
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import stylecloud
import matplotlib.pyplot as plt
from stop_words import get_stop_words
from PIL import Image

word = open('../data/stopWordList.json')
my_long_list = json.load(word)

# import .csv file to DataFrame file
df = pd.read_csv('../data/laNacion.csv', sep=',')

# convert df to dataframe
df = pd.DataFrame(df)

# covert fecha to datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# filter dataframe "df" by interval date
df = df[(df['fecha'] >= '2022-01-01') & (df['fecha'] <= '2022-12-31')]




print(len(df))

palabras = get_stop_words('spanish')

for i in range(len(my_long_list)):
    palabras.append(my_long_list[i])

my_mask = np.array(Image.open("../image/flag_argentina.webp"))
wc = WordCloud(
               colormap='winter_r',
               background_color='white',
               mask=my_mask,
               width=600,
               height=300,
               contour_width=3,
               contour_color='white', # color del contorno de la imagen
               stopwords=palabras,
               )

wc.generate(' '.join(df['titular']))
image_colors = ImageColorGenerator(my_mask)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(20, 10))
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear',alpha=1)
plt.axis('off')
wc.to_file('../output/laNacion_2021.png')
plt.show()
