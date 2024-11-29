import tweepy
import csv
import time

# Set up API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPfhxAEAAAAA7y0WTXBFXjQkuvKbssG%2B1DNCvTE%3DxwN4X99MPYcPiI8TseVz40381yVNjcHzNzZkdjf852mD6ncFtv'

# Initialize the Client
client = tweepy.Client(bearer_token=bearer_token)

# Function to fetch tweets and handle rate limits
def fetch_and_save_tweets(username, filename):
    try:
        user_data = client.get_user(username=username)
        tweets = client.get_users_tweets(id=user_data.data.id, max_results=10)
        
        # Save tweets to a CSV file
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Tweet Text'])  # Writing header
            for tweet in tweets.data:
                writer.writerow([tweet.text])  # Writing tweet content
        
        print(f"Tweets from {username} have been saved to '{filename}'")

    except tweepy.errors.TooManyRequests:
        print("Rate limit exceeded. Waiting for 15 minutes...")
        time.sleep(15 * 60)  # Wait for 15 minutes
        fetch_and_save_tweets(username, filename)  # Retry after delay
    except Exception as e:
        print(f"An error occurred: {e}")

# Fetch and save tweets
fetch_and_save_tweets('StockTwits', 'tweets.csv')
