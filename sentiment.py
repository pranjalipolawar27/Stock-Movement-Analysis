import re
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet)  
    tweet = re.sub(r"[^A-Za-z0-9 ]+", "", tweet)  
    return tweet


sia = SentimentIntensityAnalyzer()

with open('cleaned_tweets.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    next(reader)  
    tweets = [row[0] for row in reader]  
cleaned_tweets = [clean_tweet(tweet) for tweet in tweets]


sentiment_results = []
for tweet in cleaned_tweets:
    sentiment = sia.polarity_scores(tweet)  
    sentiment_results.append((tweet, sentiment['compound']))  


with open('sentiment_tweets.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Tweet Text", "Sentiment Score"])  
    for result in sentiment_results:
        writer.writerow(result)

print("Sentiment analysis complete. Results saved to 'sentiment_tweets.csv'")
