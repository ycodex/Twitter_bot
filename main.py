import tweepy as tp
from api import main
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv("keys.env")
consumer_key=str(os.getenv("consumer_key"))
consumer_secret=str(os.getenv("consumer_secret"))
access_token=str(os.getenv("access_token"))
access_token_secret=str(os.getenv("access_token_secret"))

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
api=tp.API(auth)

tweet=main()

api.update_status(tweet)

