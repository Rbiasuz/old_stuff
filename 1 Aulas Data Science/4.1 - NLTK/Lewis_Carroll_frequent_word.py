import requests
import pandas as pd
from bs4 import BeautifulSoup
import nltk
import string
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set(color_codes=True)
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
from nltk.corpus import stopwords

# Getting the Moby Dick HTML
r = requests.get('https://www.gutenberg.org/files/11/11-h/11-h.htm', verify=False)

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
print(html[0:500])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html)

# Getting the text out of the soup
text = BeautifulSoup.get_text(soup)

# Printing a part of our beloved text
print(text[3670:4480])

# Creating a tokenizer that finds only words
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens
print(tokens[0:8])


# Looping through the tokens and make them lower case
words = []
for word in tokens:
    words.append(word.lower())
words[0:5]


# Removing the stopwords
sw = stopwords.words('english')
words_ns = []
for word in words:
    if word not in sw:
        words_ns.append(word)
words_ns[0:5]



# Creating the word frequency distribution
freqdist = nltk.FreqDist(words_ns)
freqdist.most_common(30)


# What are doing gutenberg and project doing there? I also dislike some of these words:
new_stopwords = ['gutenberg', 'project', 'would', 'went', '1', 'e', 'tm', 'could', 'must']
word_final = []
for word in words_ns:
    if word not in new_stopwords:
        word_final.append(word)

# Plotting the word frequency distribution
freqdist = nltk.FreqDist(word_final)
freqdist.plot(20)

# what about bigrams?
bigrams = list(nltk.bigrams(word_final))
freqdist = nltk.FreqDist(bigrams)
freqdist.plot(25)

# what about trigrams?
trigrams = list(nltk.trigrams(word_final))
freqdist = nltk.FreqDist(trigrams)
freqdist.plot(5)



#Sentiment Analysis

#First, I'm separating the text in 15 parts (from the beginning to the end)

#returning the text to a string format
all_text = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
#here I'm at the start of the text, because the first charachters are descriptions of the site
all_text[2000:2500]
size = len(all_text)
all_text = all_text[2165:size]
size = len(all_text)
#Dividing in 15 parts
part_size = size/15
df = pd.DataFrame()
parts = []
for i in range(15):
    parts.append(all_text[int((i*part_size)):int((part_size*(i+1)))])

#turning into a dataframe (to easily manipulate
d = {'sentence':parts}
df = pd.DataFrame(d)
df

#The last two parts also are texts from the site, so we're droping it
df = df.drop(df.index[14])
df = df.drop(df.index[13])


#defining the diferent sentiment analysis methods:

analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_positive(sentence):
    score = analyser.polarity_scores(sentence)
    retorno = score.get('pos')
    return retorno

def sentiment_analyzer_negative(sentence):
    score = analyser.polarity_scores(sentence)
    retorno = score.get('neg')
    return retorno

def sentiment_analyzer_vader(sentence):
    score = analyser.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    retorno = score.get('compound')
    return retorno

def analize_sentiment_textblop(sentence):
    analysis = TextBlob(sentence)
    return analysis.sentiment.polarity

df['vader'] = df['sentence'].apply(lambda x: sentiment_analyzer_vader(x))
df['textblop'] = df['sentence'].apply(lambda x: analize_sentiment_textblop(x))
df['positive'] = df['sentence'].apply(lambda x: sentiment_analyzer_positive(x))
df['negative'] = df['sentence'].apply(lambda x: sentiment_analyzer_negative(x))


df[['positive','negative','textblop','vader']].plot(kind='bar')
plt.show()

df[['positive','textblop']].plot(kind='bar')
plt.show()

#Heatmap
df1=df.drop('sentence', axis=1)
df1=df1.drop('vader', axis=1)
df1=df1.drop('textblop', axis=1)
sns.heatmap(df1, cmap='viridis', annot=True, linewidths=0.7, square=False)
plt.show()
