import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from textblob import TextBlob
import seaborn as sns
import csv
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json

newspaper = pd.read_csv('../data/paginaSiete.csv')


"""
with open("../data/paginaSiete.csv", "r", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    i=1
    for row in reader:
        text = row[0]
        blob = TextBlob(text).translate(from_lang="es",to="en")
        print(i)
        print(text)
        print(blob.sentiment)
        i=i+1
"""

"""
# Vemos el tamaño de palabras
seq_length = [len(str(i)) for i in newspaper["titulo"]]
pd.Series(seq_length).hist(bins=70)
plt.show()
"""


"""
# Frecuencia de palabras
def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(str(text).lower())]

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

stop_words = stopwords.words('spanish')
# import json stopwords
with open('../newspaper/bolivia/data/stopWordList.json') as f:
    stopwords = json.load(f)

stop_words.extend(stopwords)

newspaper['lemmatized'] = newspaper.titulo.apply(lemmatize_text)
newspaper['lemmatized'] = newspaper['lemmatized'].apply(lambda x: [word for word in x if word not in stop_words])

# use explode to expand the lists into separate rows
wf_newspaper = newspaper.lemmatized.explode().to_frame().reset_index(drop=True)

# plot dfe
sns.countplot(x='lemmatized', data=wf_newspaper, order=wf_newspaper.lemmatized.value_counts().iloc[:20].index)
plt.xlabel('Most common used words')
plt.ylabel('Frequency [%]')
plt.xticks(rotation=70)
plt.show()
"""

## Análisis de sentimientos
newspaper['polarity'] = newspaper.titulo.apply(lambda x: TextBlob(str(x)).translate(from_lang="es",to="en").polarity)
newspaper['subjectivity'] = newspaper.titulo.apply(lambda x: TextBlob(str(x)).translate(from_lang="es",to="en").subjectivity)

print(newspaper)

