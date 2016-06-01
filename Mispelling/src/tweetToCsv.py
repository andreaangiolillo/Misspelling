#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import re
import random

#Twitter API credentials

consumer_key="F9TnxzJ3eEK4xB1hTbIYuPERa"
consumer_secret="E18qbpu8pEiQpxRzlWRW44ZmpmGwWV2zb1Y9eZ3G8vCrrIcPZP"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="250822105-ufFJci3R3aV5IALFpmzVBTrSCVIYQDsH2Nt6k7Jn"
access_token_secret="8Hfv7AN8RnSwfM6oA9KOq8loSdWwvaJiQOcq6DwY8GB0T"


def get_all_tweets(screen_name):
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

def cleanCsv():
    print "start cleanCsv"
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
                #print row[0]
                newstr = re.sub('([^a-zA-Z0-9_ # @ \%\'])', '', row[0])
                newstr = re.sub('(https)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(http)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(rt)[a-zA-Z0-9_  # @ \%\']*', '', newstr.lower())
                if len(newstr) > 0:
                    clean.append(newstr.lower())
                    

    #write the csv    
    with open('csv\clean_tweets.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([clean])
    pass
    print "end cleanCsv"


def perturbation():
    
    print "start perturbation"
    
    nameL = ["a   ", "b   ", "c   ", "d   ", "e   ", "f   ", "g   ", "h   ", "i   ", "j   ", "k   ", "l   ", "m   ", "n   ", "o   ", "p   ", "q   ", "r   ", "s   ", "t   ", "u   ", "v   ", "w   ", "x   ", "y   ", "z   "]
   
    #I modify the tweets by including only substitution error
    error = [("s","q","z"),#a
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
             ("n","k","l"),#m
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
   
    
    newStr = []
    with open('csv\clean_tweets.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            le = len(row[0])
            le= (le/10) # 10%
            if le > 0:
                str = row[0]
                letter_in_t = []
                for i in range(0,25):#kepp a characters into a string
                    if nameL[i].strip() in row[0]:
                        letter_in_t.append(nameL[i])
                        #print nameL[i]
            
                  
                #insert #le error
                for i in range(0,le):
                    #print len(letter_in_t)
                    if len(letter_in_t) > 0:
                        #print "LUIIIIIII"
                        #print le
                        lettera = random.choice(letter_in_t)     #choose a letter of the alphabet  
                        #print lettera
                        
                        for n in range(0,25):#name => number
                            if lettera == nameL[n]:
                                lettera = n
                                break
                    
                    
                        #print lettera
                        lettera_n = len(error[lettera])#num of letter's errors
                        #print lettera_n 
                    
                        r = random.randint(0,lettera_n - 1)#chose a letter's error
                        str = str.replace(nameL[lettera].strip(),error[lettera][r].strip(), 1)#insert an error
                        #print str
                        if i == le - 1:
                            newStr.append(str)
                             
                
                
    #write the csv    
    with open('csv\perturbation_tweets.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([newStr])
    pass     

    print "end perturbation"       
 