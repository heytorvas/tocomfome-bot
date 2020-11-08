import tweepy, json

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

def create_api(credentials):
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

credentials = get_credentials()
api = create_api(credentials)
search = 'fome'
number_tweets = 10000

for tweet in tweepy.Cursor(api.search, q=search).items(number_tweets):
    if not tweet.favorited:
        try:
            tweet.favorite()
            print('Tweet favorited')
        except Exception as e:
            print('Error on favorite')
    else:
        print('Tweet already favorited')

    # if not tweet.retweeted:
    #     try:
    #         tweet.retweet()
    #         print('Tweet retweeted')
    #     except Exception as e:
    #         print("Error on retweet")
    # else:
    #     print('Tweet already retweeted')
