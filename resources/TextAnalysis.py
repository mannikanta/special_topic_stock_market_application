from newspaper import Article
from textblob import TextBlob
import nltk

def download_nltk_data():
    nltk.download('punkt')  # Download the punkt tokenizer

def sentimentAnalysisCalculation(url):
    download_nltk_data()  # Make sure to download the required nltk data
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 to 1
    return sentiment


# Example usage:
url = 'https://finance.yahoo.com/m/fc90d74b-3f3a-33a3-be6f-8175704caf4d/apple-watch-asthma-tracking.html'
result = sentimentAnalysisCalculation(url)
print("Sentiment:", result)













# from textblob import TextBlob
# from newspaper import Article
# import nltk
#
# url = 'https://finance.yahoo.com/news/google-antitrust-trial-means-search-131351878.html'
# nltk.download()
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()
#
# text = article.summary
# print(text)
#
# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity # -1 to 1
# print(sentiment)