import csv
from collections import Counter

# Load cleaned tweets from CSV file
with open('cleaned_tweets.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    cleaned_tweets = [row[0] for row in reader]  # assuming the tweet text is in the first column

def extract_stock_mentions(tweets, stock_symbols):
    stock_mentions = {symbol: 0 for symbol in stock_symbols}
    for tweet in tweets:
        for symbol in stock_symbols:
            if symbol.lower() in tweet.lower():
                stock_mentions[symbol] += 1
    return stock_mentions

stock_symbols = ['Tesla', 'Apple', 'Amazon', 'Google']
mentions = extract_stock_mentions(cleaned_tweets, stock_symbols)

# Print stock mentions
print(mentions)
