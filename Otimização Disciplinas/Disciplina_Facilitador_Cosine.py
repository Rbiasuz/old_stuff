import nltk
import re
import time
import numpy as np
import matplotlib.pyplot as plt
import math
from collections import Counter

# nltk.download('stopwords')

#with open("Text_Mining1/disc_unic.csv") as f:
with open("disc_unic.csv") as f:
    discipline = f.read()
discipline = discipline.splitlines()
#with open("Text_Mining1/emen_unic.csv") as f:
with open("emen_unic.csv") as f:
    ementa = f.read()
ementa = ementa.splitlines()

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

# Definindo stopwords
stopwords = set(nltk.corpus.stopwords.words('portuguese'))

linha = 0
for x in ementa:
    # Minusculando
    ementa[linha] = x.lower()
    # Tirando pontuação do meio
    ementa[linha] = re.sub(r'[^\w\s]',' ',ementa[linha], re.UNICODE)
    # Tirando Stopwords
    for word in stopwords:
        ementa[linha] = ementa[linha].replace(" " + word + " ", " ")
    linha += 1

#Quantas disciplinas mostrar no gráfico?
nrovisual = 10

top = np.zeros(nrovisual, dtype='object')
topvalue = np.zeros(nrovisual)
comp_list = np.zeros(len(ementa))


print('''Olá! 
Eu Sou o Disciplina Facilitador!!
Digite sua ementa e eu vou encontrar disciplinas similares a sua!
Obs. Pode escrever:''')

nova = input()

while True:
    if nova == "fim":
        break

# Pesquisa Operacional. Programação Linear suporte para a tomada de decisões, análise gráfica método Simplex e Dinâmica.
    t = time.process_time()

    nova = nova.lower()
    nova = re.sub(r'[^\w\s]', ' ', nova, re.UNICODE)
    for word in stopwords:
        nova = nova.replace(" " + word + " ", " ")

    for x in range(len(ementa)):
        comp_list[x] = get_result(nova, ementa[x])

    order = np.argsort(comp_list)[::-1]

    for x in range(nrovisual):
        top[x] = discipline[order[x]]
        topvalue[x] = comp_list[order[x]]

    fig, ax = plt.subplots(num=None, figsize=(7, 5), facecolor='w', edgecolor='k')
    ax.plot(top, topvalue, lw=2, color='purple')
    ax.grid(True)
    fig.autofmt_xdate()
    plt.title('Ementas Semelhantes a sua!')
    plt.show()

    elapsed_time = time.process_time() - t
    print(elapsed_time)

    print('''Seu gráfico foi gerado!
Se quiser procurar mais alguma ementa é só digitar!
Por outro lado, se está satisfeito, escreva "fim" e o programa será encerrado!!''')
    nova = input()

print('''Muito obrigado por me usar =) 
Tenha um ótimo dia!!''')
