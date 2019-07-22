import nltk
import re
import numpy as np
from collections import Counter
import math
import pandas as pd

with open("d_teste.csv") as f:
    discipline = f.read()

discipline = discipline.splitlines()

with open("e_teste.csv") as f:
    ementa = f.read()

ementa = ementa.splitlines()

linha = 0

# Definindo stopwords
stopwords = set(nltk.corpus.stopwords.words('portuguese'))

#Cosine método sendo definido:
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

for x in ementa:
    # Minusculando
    ementa[linha] = x.lower()
    # Tirando pontuação do meio
    ementa[linha] = re.sub(r'[^\w\s]',' ',ementa[linha], re.UNICODE)
    # Tirando Stopwords
    for word in stopwords:
        ementa[linha] = ementa[linha].replace(" " + word + " ", " ")
    linha += 1

# Inicializando matriz pra ganhar tempo
comp_matriz = np.zeros(shape=(len(ementa),len(ementa)))

#Laço principal
for x in range(len(ementa)):
    for y in range(x,len(ementa)):
        comp_matriz[x][y]= get_result(ementa[x], ementa[y])
        if comp_matriz[x][y] > 0.8 and x != y:
            print('Deu match: \033[1m {} e {} de {} pontos =) !!'.format(discipline[x],discipline[y],comp_matriz[x][y]))

df = pd.DataFrame(comp_matriz)
df.to_csv("comp_teste.csv", header=None, index=None)