import tweepy, json
from time import sleep
from datetime import datetime
from translate import Translate

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

def create_api(credentials):
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def twitter_rates():
    returned = 0
    stats = api.rate_limit_status() 
    for akey in stats['resources'].keys():
        if type(stats['resources'][akey]) == dict:
            for anotherkey in stats['resources'][akey].keys():
                if type(stats['resources'][akey][anotherkey]) == dict:
                    limit = (stats['resources'][akey][anotherkey]['limit'])
                    remaining = (stats['resources'][akey][anotherkey]['remaining'])
                    used = limit - remaining
                    if used != 0:
                        print("Twitter API used", used, "remaining queries", remaining,"for query type", anotherkey)
                        returned = int(remaining)
                    else:
                        pass
                else:
                    pass 
        else:
            print(akey, stats['resources'][akey])
            print(stats['resources'][akey].keys())
            limit = (stats['resources'][akey]['limit'])
            remaining = (stats['resources'][akey]['remaining'])
            used = limit - remaining
            if used != 0:
                print("Twitter API:", used, "requests used,", remaining, "remaining, for API queries to", akey)
                returned = int(remaining)
                pass
    
    return returned

t = Translate()
search = t.read_txt_file()
number_tweets = 8
count = 0
print('Words done')

api = create_api(get_credentials())
remaining = twitter_rates()
print('API done')

while True:

    api = create_api(get_credentials())

    for word in search:
        for tweet in tweepy.Cursor(api.search, q=word).items(number_tweets):
            if count == remaining:
                print('Sleep')
                sleep(60*15)
                count = 0
                api = create_api(get_credentials())
                remaining = twitter_rates()
                print('API done')

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