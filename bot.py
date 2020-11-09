import tweepy, json
from time import sleep
from translate import Translate

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

def create_api(credentials):
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

t = Translate()
search = t.read_txt_file()
number_tweets = 8
count = 0
print('Words done')

while True:

    if count > 170:
        print('Sleep')
        sleep(60*15)
        count = 0

    api = create_api(get_credentials())
    print('API done')

    for word in search:
        for tweet in tweepy.Cursor(api.search, q=word).items(number_tweets):
            try:
                tweet.favorite()
                print('Tweet liked')
                count += 1
        
            except tweepy.TweepError as e:
                if str(e.reason) == 'Twitter error response: status code = 429' :
                    print(e.reason)
                    count += 1
                    continue
                else:
                    print(e.reason)
                    count += 1
                    continue
                
            except StopIteration:
                break

        print(word, ' done')