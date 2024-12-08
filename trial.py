import tweepy
import time
import csv


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPfhxAEAAAAA7y0WTXBFXjQkuvKbssG%2B1DNCvTE%3DxwN4X99MPYcPiI8TseVz40381yVNjcHzNzZkdjf852mD6ncFtv'


client = tweepy.Client(bearer_token=bearer_token)


usernames = ['Moneycontrol', 'EconomicTimes', 'ZeeBusiness', 'livemint', 'ETNOWlive']


with open('twitter1.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Tweet"])  

   
    for username in usernames:
        print(f"Fetching tweets from {username}...\n")
        
        try:
           
            user_data = client.get_user(username=username)
            if user_data and user_data.data:
                tweets = client.get_users_tweets(id=user_data.data.id, max_results=10, tweet_fields=["lang"])
                
                
                if tweets.data:
                    for tweet in tweets.data:
                        if tweet.lang == 'en':  
                            writer.writerow([username, tweet.text])
                            print(f"Stored tweet from {username}: {tweet.text}\n")
                        else:
                            print(f"Skipped tweet from {username} (not in English).\n")
                else:
                    print(f"No tweets available for {username}.\n")
            else:
                print(f"User data not found for {username}.\n")

        except tweepy.errors.TooManyRequests:
            print(f"Rate limit exceeded for {username}. Waiting to retry...\n")
            time.sleep(15 * 60)  
        except tweepy.errors.TweepyException as e:
            print(f"An error occurred for {username}: {e}\n")

print("All  tweets have been saved to 'twitter.csv'")
