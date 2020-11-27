# import datetime
# import logging

# import azure.functions as func

# import tweepy 

# # from config import create_api

# import time
# import os

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()

# def create_api():
#     consumer_key = os.environ("CONSUMER_KEY")
#     consumer_secret = os.environ("CONSUMER_SECRET")
#     access_token = os.environ("ACCESS_TOKEN")
#     access_token_secret = os.environ("ACCESS_TOKEN_SECRET")

#     auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
#     auth.set_access_token(access_token,access_token_secret)

#     api = tweepy.API(auth)

#     try:
#         api.verify_credentials()
#     except Exception as e:
#         logging.error("Error creating api", exc_info=True)
#         raise e

#     logger.info("API created")
#     return api 


# # class FavRetweetListener(tweepy.StreamListener):
# #     def __init__(self,api):
# #         self.api = api 
# #         self.me = api.me()



#     # def on_status(self, tweet):
#     #     logger.info(f"Processing tweet id {tweet.id}")
#     #     if tweet.in_reply_to_status_id is not None or \
#     #         tweet.user.id == self.me.id:
#     #         # This tweet is a reply or I'm its author so, ignore it
#     #         return
#     #     if not tweet.favorited:
#     #         # Mark it as Liked, since we have not done it yet
#     #         try:
#     #             tweet.favorite()
                

#     #         except Exception as e:
#     #             logger.error("Error on fav", exc_info=True)
#     #     if not tweet.retweeted:
#     #         # Retweet, since we have not retweeted it yet
#     #         try:
#     #             tweet.retweet()
                
#     #         except Exception as e:
#     #             logger.error("Error on fav and retweet", exc_info=True)

#     # def on_error(self, status):
#     #     logger.error(status)

# def twittermain(keywords):
#     api = create_api()
#     # tweets_listener = FavRetweetListener(api)
#     # stream = tweepy.Stream(api.auth, tweets_listener)
#     # stream.filter(track=keywords, languages=["en"])
#     # time.sleep(100)
#     # stream.disconnect()
#     today = str(datetime.date.today())    

#     while True :
#         for tweet in tweepy.Cursor(api.search,q=keywords, lang="en", since=today).items(1):
#             try:
#                 api.retweet(tweet.id)
#             except:
#                 pass
#             try:
#                 api.create_friendship(tweet.user.id)
#             except:
#                 pass
#         return
    


# def main(mytimer: func.TimerRequest) -> None: 
#     utc_timestamp = datetime.datetime.utcnow().replace(
#         tzinfo=datetime.timezone.utc).isoformat()

#     if mytimer.past_due:
#         logging.info('The timer is past due!')

#     logging.info('Python timer trigger function ran at %s', utc_timestamp)

#     twittermain(["spacex","isro"])
#     logging.info('Python timer trigger function ran at %s', utc_timestamp)


import tweepy, time, datetime, logging, os
from datetime import date
import azure.functions as func
import random
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)
    logging.info("Api created")
    today = str(date.today())

    keywords = ["#space","#spacex","#isro","#telescope","#spacetime","#outerspace"]
    value = random.randint(1,6)

    
    for tweet in tweepy.Cursor(api.search,q=["#space"], lang="en", since=today).items(1):
        try:
            api.retweet(tweet.id)
            logging.info(f"Retweeting: {tweet.id}")
        except Exception as e:
            
            logging.error(f"Error occured at retweeting : {e}")
            
        try:
            api.create_friendship(tweet.user.id)
            logging.info(f"Creating friendship: {tweet.user.id}")
        except Exception as e:
            
            logging.error(f"Error occured at tweet user id  : {e}")
                     
    # except Exception as e:
    #     logging.error(e)
        