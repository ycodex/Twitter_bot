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



def count_cases(key):

    tweet=main()
    try:
        key.update_status(tweet)
    except Exception as e:
        pass
    time.sleep(86400)
def news_post(key):
    d,t=news.req()
    if(news.read_and_compare(d)):
        tweets=news.post(t)
        try:
            key.update_status(tweets)
        except Exception as e:
            pass
        time.sleep(43200)


if __name__=='__main__':
    while True:
        apis=auth()
        count_cases(apis)
        news_post(apis)
        
