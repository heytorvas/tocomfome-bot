import tweepy

def create_api():
    consumer_key = 'ULHZe5DSRwgVSRnt1GfGryPJ7'
    consumer_secret = 'LkZSKjQJcpYSeAMLpMwmO2DOH7AeAk1uOPTuMMy5mpy5NJO0tJ'
    access_token = '1325440467794845696-MYdZTSweTAXUjP9yxuIkhjismP1oEQ'
    access_token_secret = 'K07kT6mb2gm6ngTwSEdZB56nK1CfFjDqZiJHgq7gMARXK'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if not tweet.favorited:
            try:
                tweet.favorite()
                print('Tweet favorited')
            except Exception as e:
                print("Error on fav")
        if not tweet.retweeted:
            try:
                tweet.retweet()
                print('Tweet retweeted')
            except Exception as e:
                print("Error on retweet")

    def on_error(self, status):
        print("Error: ", status)

api = create_api()
tweets_listener = FavRetweetListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=['fome', 'faminto'], languages=["pt"])