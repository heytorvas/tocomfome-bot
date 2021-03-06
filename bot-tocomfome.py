# -*- coding: utf-8 -*-

import tweepy, json
from time import sleep

def get_credentials():
    with open('config.json') as config_file:
        return json.load(config_file)

def get_words():
    f = open('words.txt', 'r')
    return list(f)

def read_txt_file():
    txt_list = ''
    with open("words.txt","r") as f:
        txt_list = f.readlines()
        f.close()
    
    words_list = []
    for i in txt_list:
        words_list.append(i.replace('\n', ''))

    return words_list

def create_api(credentials):
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def tweet(phrase):
    try:
        api.update_status(phrase)
        print('Tweet done')
        sleep(60*60*2)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(60*60*2)

while True:
    api = create_api(get_credentials())
    print('API done')

    phrases = read_txt_file()

    for phrase in phrases:
        tweet(phrase)