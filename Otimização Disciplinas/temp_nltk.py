import nltk
from nltk.stem import RSLPStemmer
import re
import numpy as np
from collections import Counter
import math
import pandas as pd
from unicodedata import normalize

mystopwords = {'ao', 'estivessem', 'num', 'já', 'I', 'houvessem', 'contudo', 'seus', 'estivera', 'houveremos', 'por', 'e', 'vos', 'todo', 'essas', 'haja', 'nós', 'outros', 'teve', 'houveríamos', 'foi', 'sejam', 'sejamos', 'tenho', 'dispoem', 'pois', 'sendo', 'aonde', 'estava', 'mesmas', 'tuas', 'um', 'aos', 'tinham', 'pela', 'tivera', 'terei', 'III', 'nas', 'estes', 'estiverem', 'pelo', 'estou', 'houvéramos', 'sou', 'tivéssemos', 'contra', 'demais', 'nossos', 'teu', 'conclusão', 'delas', 'fui', 'o', 'houveram', 'este', 'que', 'VI', 'cujo', 'os', 'teríamos', 'logo', 'suas', 'tivemos', 'se', 'estejamos', 'teria', 'durante', 'III:', 'uma', 'mais', 'teus', 'esse', 'tem', 'diversas', 'qual', 'tambem', 'quem', 'houverei', 'mas', 'houvéssemos', 'ha', 'isso', 'fora', 'hão', 'tal', 'das', 'estivéssemos', 'tivesse', 'aquele', 'ambas', 'de', 'éramos', 'dele', 'estiver', 'seria', 'cujos', 'antes', 'tém', 'me', 'curso', 'V', 'pelas', 'teriam', 'perante', 'quando', 'outro', 'houvermos', 'formos', 'mesmo', 'houvesse', 'sob', 'neste', 'estivermos', 'será', 'houve', 'I:', 'II:', 'quer', 'houveria', 'forem', 'estiveram', 'tenham', 'tiverem', 'todas', 'diversos', 'pelos', 'às', 'desta', 'esteve', 'tiver', 'nesse', 'minha', 'ambos', 'nos', 'lhes', 'isto', 'hei', 'nossas', 'numa', 'nosso', 'serei', 'aquilo', 'terá', 'assim', 'não', 'minhas', 'tiveram', 'terão', 'a', 'no', 'tivessem', 'serão', 'estivesse', 'depois', 'cuja', 'ela', 'ainda', '-', 'for', 'propios', 'houvemos', 'houverão', 'diversa', 'com', 'fomos', 'proprio', 'seu', 'dispõe', 'sem', 'IV:', 'está', 'estive', 'aquela', 'cujas', 'temos', 'além', 'havemos', 'tivermos', 'quanto', 'sua', 'desde', 'do', 'nem', 'muito', 'estágio', 'qualquer', 'tudo', 'estejam', 'estas', 'foram', 'as', 'elas', 'outra', 'estávamos', 'houverá', 'aqueles', 'houveriam', 'dos', 'também', 'hajam', 'porque', 'te', 'tinha', 'você', 'mesma', 'em', 'estamos', 'teremos', 'seríamos', 'deste', 'estavam', 'é', 'deles', 'há', 'quais', 'hajamos', 'eram', 'houver', 'esses', 'meus', 'tenha', 'da', 'para', 'houvera', 'mediante', 'entre', 'na', 'essa', 'fossem', 'mesmos', 'todos', 'como', 'lhe', 'estivemos', 'meu', 'eles', 'fôramos', 'seremos', 'II', 'fôssemos', 'à', 'esta', 'dela', 'seja', 'só', 'tivéramos', 'eu', 'após', 'somos', 'fosse', 'ele', 'IV', 'entao', 'menos', 'era', 'tenhamos', 'toda', 'sobre', 'estão', 'seriam', 'tínhamos', 'tu', 'portanto', 'esteja', 'são', 'até', 'nossa', 'estivéramos', 'tua', 'outras', 'tive', 'ou', 'aquelas', 'houverem', 'vocês'}
df = pd.read_excel('Teste120.xlsx')
df_new = df.copy()

def rem_acento(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def get_result(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase



df_new['EMENTA'].str.lower()
df_new = df_new.apply(rem_acento)

for x in range(len(df_new)):
    df_new.iloc[x][1] = rem_acento(df_new.iloc[x][1])
    df_new.iloc[x][1] = re.sub(r'[^\w\s]', ' ', df_new.iloc[x][1], re.UNICODE)
    for word in mystopwords:
        df_new.iloc[x][1] = df_new.iloc[x][1].replace(" " + word + " ", " ")

df2 = df_new.copy()

for x in range(len(df2)):
    df2.iloc[x][1] = Stemming(Tokenize(df2.iloc[x][1]))
    df2.iloc[x][1] = " ".join(df2.iloc[x][1])

matriznormal = np.zeros(shape=(len(df_new),len(df_new)))
matriznormalcont = 0
matrizlematizada = np.zeros(shape=(len(df_new),len(df_new)))
matrizlematizadacont = 0

for x in range(len(df_new)):
    for y in range(x,len(df_new)):
        matriznormal[x][y]= get_result(df_new.iloc[x][1], df_new.iloc[y][1])
        if matriznormal[x][y] > 0.7 and x != y:
            matriznormalcont +=1

for x in range(len(df2)):
    for y in range(x,len(df2)):
        matrizlematizada[x][y]= get_result(df2.iloc[x][1], df2.iloc[y][1])
        if matrizlematizada[x][y] > 0.7 and x != y:
            matrizlematizadacont +=1

print(matriznormalcont)
print(matrizlematizadacont)


mnormal = pd.DataFrame(matriznormal)
mlematizada = pd.DataFrame(matrizlematizada)

mnormal.to_csv("mnormal.csv", header=None, index=None)
mlematizada.to_csv("mlematizada.csv", header=None, index=None)
