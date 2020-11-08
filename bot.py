import tweepy, json

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

credentials = get_credentials()

auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'fome'
number_tweets = 10

for tweet in tweepy.Cursor(api.search, q=search).items(number_tweets):
    if not tweet.favorited:
        try:
            tweet.favorite()
            print('Tweet liked')
        except tweepy.TweepError as e:
            print('Error on like')
    else:
        print('Tweet already favorited')
