#!/usr/bin/python2
#
# mpd-twitter: Publish on twitter what you are listening on MPD 
#

import ConfigParser, os
from twitter import Api

config = ConfigParser.ConfigParser()
params = config.readfp(open(os.environ['HOME'] + '/.mpd-twitter'))
CONSUMER_KEY = config.get('connect_params', 'CONSUMER_KEY', 1)
CONSUMER_SECRET = config.get('connect_params', 'CONSUMER_SECRET', 1)
ACCESS_TOKEN_KEY = config.get('connect_params', 'ACCESS_TOKEN_KEY', 1)
ACCESS_TOKEN_SECRET = config.get('connect_params', 'ACCESS_TOKEN_SECRET', 1)

TWEET_BEFORE = config.get('tweet_params', 'BEFORE', 1)
TWEET_AFTER = config.get('tweet_params', 'AFTER', 1)

api = Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

t,current_song = os.popen4('mpc current')
status = TWEET_BEFORE + ' ' + current_song.read().rstrip() + ' ' + TWEET_AFTER

new_status = api.PostUpdate(status)
