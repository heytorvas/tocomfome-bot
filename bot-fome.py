import tweepy, json
from translate import Translate

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

def create_api(credentials):
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    print("API created")
    return api

class FavListener(tweepy.StreamListener):

    def on_status(self, status):

        number = 1
        search = 'fome'

        for tweet in tweepy.Cursor(api.search, search, since='2020-11-09').items():
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    print("Tweet liked with id {}".format(tweet.id))
                except Exception as e:
                    print("Tweet error with id {}".format(tweet.id))

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    # t = Translate()
    # words = t.read_txt_file()
    # words = 'fome'
    # main(words)

    streamer = FavListener()
    api = create_api(get_credentials())
    stream = tweepy.Stream(auth=api.auth, listener=FavListener())
    stream.filter(track=['fome'], )