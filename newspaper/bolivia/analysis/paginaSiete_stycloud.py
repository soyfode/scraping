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

with open("../data/paginaSiete_titulo.txt", "r") as csv_file:
    text = csv_file.read()

palabras = get_stop_words('spanish')

for i in range(len(my_long_list)):
    palabras.append(my_long_list[i])

my_mask = np.array(Image.open("../image/periodico.jpg"))
wc = WordCloud(
               colormap='winter_r',
               background_color='#F5F2E8',
               mask=my_mask,
               width=600,
               height=300,
               contour_width=3,
               contour_color='#F5F2E8', # color del contorno de la imagen
               stopwords=palabras,
               )

wc.generate(text)
image_colors = ImageColorGenerator(my_mask)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(20, 10))
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear',alpha=1)
plt.axis('off')
wc.to_file('../output/paginaSiete_stycloud_papercolor.png')
plt.show()
