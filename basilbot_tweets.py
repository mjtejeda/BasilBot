import tweepy
import os
from time import sleep
from credentials import *

#access and authorize twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'facts.txt')

my_file = open(filename, 'r')

file_lines = my_file.readlines()

my_file.close()

for line in file_lines:
    print(line)
    
    if line != '\n':
        api.update_status(line)
        
    else:
        pass
    
    sleep(300)

