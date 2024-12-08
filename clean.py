import re
import csv

def clean_tweet(tweet):
    
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet)  
    tweet = re.sub(r"[^A-Za-z0-9 ]+", "", tweet)  
    return tweet


with open('twitter1.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    next(reader)  
    tweets = [row[0] for row in reader]


cleaned_tweets = [clean_tweet(tweet) for tweet in tweets]

with open('cleaned_tweets.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Tweet Text"]) 
    for tweet in cleaned_tweets:
        writer.writerow([tweet]) 

print("Tweets have been cleaned and saved to 'cleaned_tweets.csv'")
