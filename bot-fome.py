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
        print("Error creating API", exc_info=True)
        raise e
    print("API created")
    return api

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print("Processing tweet id {}".format(tweet.id))
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                print("Error on fav")

    def on_error(self, status):
        print(status)

def main(words):
    api = create_api(get_credentials())
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=words)

if __name__ == "__main__":
    # t = Translate()
    # words = t.read_txt_file()
    words = 'fome'
    main(words)