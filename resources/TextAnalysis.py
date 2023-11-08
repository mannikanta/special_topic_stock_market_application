from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://finance.yahoo.com/news/google-antitrust-trial-means-search-131351878.html'
nltk.download()
article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)