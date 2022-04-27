import tweepy
from credentials import *
from mastodon import Mastodon
#setup tweepy
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token_tweepy, access_token_secret)
mastodon = Mastodon(access_token = mastodon_token ,api_base_url = mastodon_url)

def main():
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    tweet = '\n'.join(contents)

    print("would you like to tweet:")
    print("-----------------")
    print(tweet)

    x = input("y/n: ")

    if x.lower() == "y":
        print("tweet sendt")
        client.create_tweet(text=tweet)
        mastodon.toot(tweet)
    elif x.lower() == "n":
        print("tweet not sendt")
    else:
        print(x, " is an unknown command")
if __name__ == '__main__':
    main()
