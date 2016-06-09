#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import re
import random
from ground_truth import isletter
from numpy.random.mtrand import randint




import ground_truth

#Twitter API credentials

consumer_key="F9TnxzJ3eEK4xB1hTbIYuPERa"
consumer_secret="E18qbpu8pEiQpxRzlWRW44ZmpmGwWV2zb1Y9eZ3G8vCrrIcPZP"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="250822105-ufFJci3R3aV5IALFpmzVBTrSCVIYQDsH2Nt6k7Jn"
access_token_secret="8Hfv7AN8RnSwfM6oA9KOq8loSdWwvaJiQOcq6DwY8GB0T"


class TweetToCsv:
    
    error_list = [("s","q","z"),#a
                      ("v","n","h","g"),#b
                      ("x","v","f","d"),#c
                      ("s","f","x","e"),#d
                      ("w","r","d"),#e
                      ("d","g","c","r","t"),#f
                      ("f","h","v","t","y"),#g
                      ("g","j","b","y","u"),#h
                      ("u","o","k"),#i
                      ("h","k","n","u"),#j
                      ("j","l","m","i","o"),#k
                      ("k","o","p","m"),#l
                      ("j","k","l"),#m
                      ("b","m","j","h"),#n
                      ("i","p","k","l"),#o
                      ("o","l"),#p
                      ("w","a"),#q
                      ("e","t","d","f"),#r
                      ("a","d","z","w","e"),#s
                      ("r","y","f","g"),#t
                      ("y","i","h","j"),#u
                      ("c","b","g"),#v
                      ("q","e","a","s"),#w
                      ("z","c","d","s"),#x
                      ("t","u","g","h"),#y
                      ("x","s","a")#z
                 ]

    def __init__(self):
        pass    
        
    def get_all_tweets(self, screen_name):
        
        print "start get_all_tweets"
        
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
        
        #write the csv    
        with open('csv\%s_tweets.csv' % screen_name, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(outtweets)
            pass
        print "end get_all_tweets"

    
    
    def cleanCsv(self):
        print "Start cleanCsv"
    #set a csv number
        
    
    #list with name of csv   
        #name = ["BBCBreaking","WSJPolitics","NBA","nytimes","Pontifex","POTUS","SkyFootball","UN","WSJ","WWF"]  
        name = ["UKLabour", "Conservatives", "David_Cameron", "MayorofLondon", "UniofOxford","Cambridge_Uni"]
        length = len(name)
        clean = []

        for i in range(0,length): #length): #for all csv
            with open('csv\%s_tweets.csv' % name[i], 'rb') as f:    
                reader = csv.reader(f)
            
            #clean rows
                for row in reader:
                #print row[0]
                    newstr = row[0].strip().lower()
                    newstr = re.sub('([^a-zA-Z0-9_ # @ \- \'])', '', newstr.strip())
                    newstr = re.sub('([^a-z # @ \- \'])', '', newstr.strip())
                    newstr = re.sub('-', ' ', newstr.strip())
                    newstr = re.sub('\'', '', newstr.strip())
                    newstr = re.sub('\"', '', newstr.strip())
                    newstr = re.sub('(https)[a-z  # @ \%\']*', '', newstr.strip())
                    newstr = re.sub('(http)[a-zA-Z0-9_  # @ \%\']*', '', newstr.strip())
                    newstr = re.sub('(@[a-z]*)', '', newstr.strip())
                    newstr = re.sub('(#[a-z]*)', '', newstr.strip())
                    newstr = re.sub('(^rt\s[a-z \s]*)', '', newstr.strip())
                    newstr = re.sub('nan', '', newstr.strip())
                    newstr = re.sub('inf', '', newstr.strip())
                    newstr = re.sub('^rt', '', newstr.strip())
                    newstr = newstr.strip()
                    if len(newstr) > 0:
                        clean.append(newstr.lower().strip())
                    

    #write the csv    
        with open('csv\clean_tweets.csv', 'wb') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerows([clean])
            pass
        print "End cleanCsv"
     
    
    
        with open('csv\clean_tweets.csv', 'rb') as f:
            reader = csv.reader(f)
            ns = []
            for line in reader:
                r = re.sub("\s\s+" , " ", line[0].strip())
                ns.append(r)
                
        with open('csv\clean_tweets.csv', 'wb') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerows([ns])
        
    
    
    

    def perturbate_tweets(self): 
        print "Start perturbation"
        riscrittura = []
        with open('csv\clean_tweets.csv', 'rb') as r:
            reader = csv.reader(r)
            for line in reader:
                tweet = line[0]
                for i in range(len(tweet)):
                    if isletter(tweet[i]):
                        r = random.random()
                        if r < 0.1:
                            r_index = random.randint(0, len(self.error_list[ord(tweet[i])-97]) - 1)
                            tweet = tweet[:i] + self.error_list[ord(tweet[i])-97][r_index] + tweet[i+1:]
                    if i == len(tweet)-1:
                        riscrittura.append(tweet)
     
        with open('csv\perturbation_tweets.csv', 'wb') as w:
            writer = csv.writer(w, delimiter='\n')
            writer.writerows([riscrittura])                       
        print "End perturbation"
    
    """def print_tweets(self):
        output_viterbi = open('csv\output_tweets.csv')
        concatenator = []
        for line in output_viterbi:
            for word in line.split():
                if word == "Mispelling-start":
                    concatenator.append(' ')
                else:
                    concatenator.append(line)
        #concatenator = ''.join(concatenator)


        with open('csv\oooooooo.csv', 'wb') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerows([concatenator])
        pass"""