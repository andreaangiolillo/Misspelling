#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import re


#Twitter API credentials

consumer_key="F9TnxzJ3eEK4xB1hTbIYuPERa"
consumer_secret="E18qbpu8pEiQpxRzlWRW44ZmpmGwWV2zb1Y9eZ3G8vCrrIcPZP"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="250822105-ufFJci3R3aV5IALFpmzVBTrSCVIYQDsH2Nt6k7Jn"
access_token_secret="8Hfv7AN8RnSwfM6oA9KOq8loSdWwvaJiQOcq6DwY8GB0T"


def get_all_tweets(screen_name):
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets gefore %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[ tweet.text.encode("utf-8")] for tweet in alltweets]
    print outtweets
    
    #write the csv    
    with open('csv\%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass


def cleanCsv():
    #set a csv number
    length = 9 
    
    #list with name of csv   
    name = ["BBCBreaking","WSJPolitics","NBA","nytimes","Pontifex","POTUS","SkyFootball","UN","WSJ","WWF"]  
    clean = []
  
    for i in range(0,length): #length): #for all csv
        with open('csv\%s_tweets.csv' % name[i], 'rb') as f:    
            reader = csv.reader(f)
            
            #clean rows
            for row in reader:
                print row[0]
                newstr = re.sub('([^a-zA-Z0-9_ # @ \%\'])', '', row[0])
                newstr = re.sub('(https)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(http)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                clean.append(newstr)
                print newstr

    #write the csv    
    with open('csv\clean_tweets.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([clean])
    pass

print "end tweetToCsv"



        
        