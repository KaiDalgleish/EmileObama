import sys
import os
import twitter
from markov import *


# Twitter authentication
api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


#print api.VerifyCredentials()

filenames = sys.argv[1:]

generator = MarkovMachine()
generator.read_files(filenames)
print generator.make_text()

#tweet_text = 