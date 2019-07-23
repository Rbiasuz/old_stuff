from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

df = pd.read_csv('lideranca2.csv', sep=';', encoding='ISO-8859-1', engine='python')

#df = pd.read_csv('AR.csv', sep=';', encoding='ISO-8859-1')

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    retorno = score.get('compound')
    return retorno

def analize_sentiment(textopt):
    analysis = TextBlob(textopt)
    if analysis.detect_language() != 'en':
        analysis = TextBlob(str(analysis.translate(to='en')))
        return analysis.sentiment.polarity
    else:
        return analysis.sentiment.polarity

def textfunc(x):
    analysis = TextBlob(x)
    return analysis.sentiment.polarity


def sentiment(x):
    if x >= 0.25:
        return 'positive'
    elif x >= 0.20:
        return 'neutral'
    else:
        return 'negative'

df['polarity'] = df['Answers'].apply(lambda x: textfunc(x))

#df['polarity'] = df['Answers'].apply(lambda x: analize_sentiment(x))

df['polarity'] = df['Answers'].apply(lambda x: sentiment_analyzer_scores(x))

df['sentiment'] = df['polarity'].apply(lambda x: sentiment(x))


# plot chart
df.sentiment.value_counts(sort=False).plot.pie(autopct='%2.0f%%')
plt.show()

df.to_csv(df, sep=';', encoding='ISO-8859-1')

df.to_csv('results.csv', index=False, header=False)

df['polarity'].plot(kind='hist')
plt.show()