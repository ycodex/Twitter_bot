import tweepy as tp
from api import main
import os
from dotenv import load_dotenv,find_dotenv
import news
import random
import time



def auth():
    load_dotenv("keys.env")
    consumer_key=str(os.getenv("consumer_key"))
    consumer_secret=str(os.getenv("consumer_secret"))
    access_token=str(os.getenv("access_token"))
    access_token_secret=str(os.getenv("access_token_secret"))

    auth=tp.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret) 
    
    api=tp.API(auth)
    return api



def choose(key):
    option=random.randint(0,1)
    if(option==0):
        tweet=main()
        key.update_status(tweet)
    else:
        d,t=news.req()
        if(news.read_and_compare(d)):
            tweets=news.post(t)
            key.update_status(tweets)
        else:
            tweet=main()
            key.update_status(tweet)


if __name__=='__main__':
    while True:
        apis=auth()
        choose(apis)
        time.sleep(86400)
