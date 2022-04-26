import tweepy
from credentials import *
#setup tweepy
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)


tweet = input("compose tweet: ")

print("would you like to tweet:")
print("-----------------")
print(tweet)

x = input("y/n: ")

if x == "y":
    print("tweet sendt")
    client.create_tweet(text=tweet)
elif x == "n":
    print("tweet not sendt")
else:
    print(x, " is an unknown command")
