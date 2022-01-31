

# import modules
import json
import tweepy
import os


def printtweetdata(n, ith_tweet, scraped_data):
    
    d = {"Tweet Scraped":n,"Username": ith_tweet[0], "Description":ith_tweet[1],"Location":ith_tweet[2],"Following Count": ith_tweet[3], "Follower Count": ith_tweet[4],"Total Tweets":ith_tweet[5],"Retweet Count": ith_tweet[6], "Tweet Text":ith_tweet[7], "Hashtags Used": ith_tweet[8]}

    print(f"Tweet Scraped{n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")
    scraped_data.append(d)
    try:
        if not os.path.isdir('output'):
            os.mkdir('output')
        with open(f'output/scraped_data.json', 'w') as outfile:
            json.dump(scraped_data, outfile, indent=4)
    except:
        print("An exception occurred")


def scrape(words, numtweet, scraped_data):

    tweets = tweepy.Cursor(api.search_tweets, q=words, lang="en",
                           tweet_mode='extended').items(numtweet)

    list_tweets = [tweet for tweet in tweets]

    i = 1

    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]

        printtweetdata(i, ith_tweet, scraped_data)
        i = i+1


if __name__ == '__main__':
    f = open('auth.json')
    data = json.load(f)
    access_token = data["access_token"]
    access_token_secret = data["access_token_secret"]
    consumer_key = data["consumer_key"]
    consumer_secret = data["consumer_secret"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Enter Twitter HashTag to search for")
    words = input()

    print("Enter Number of tweets to be scraped")
    numtweet = int(input())
    scraped_data = []
    print("Fetching tweets...")
    scrape(words, numtweet, scraped_data)
    print('Scraping has completed!')



    
    

    

    
        

        
        
        

        
        
        



    
    

    

    
    
    
