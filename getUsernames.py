import os
import tweepy
from tweepy import OAuthHandler
from api_settings import *
import time
with open('verified_users.txt') as fr:
	content = fr.readlines()
	for lines in content:
		lines = lines.replace('\n','')
		print "Working for user:" + lines
		friends = []
		consumer_key, consumer_secret, access_token, access_token_secret = populate_Settings(\
		sys.argv[1], sys.argv[2])
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
			

		for page in tweepy.Cursor(api.friends_ids, id=lines).pages():
		    friends.extend(page)
		    print len(friends)
		    time.sleep(60)
		print "Writing to file for user id:" + str(lines)
		with open('friends.txt','a+') as fww:
			fww.write(str(lines) + "," + str(friends) + "\n")
