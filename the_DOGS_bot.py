import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('Dogs')

# iterates over pictures in models folder
for Dog_image in os.listdir('.'):
    api.update_with_media(Dog_image)
    time.sleep(3)
