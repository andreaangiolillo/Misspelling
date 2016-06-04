#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import re
import random
from random import randint

import ground_truth

#Twitter API credentials

consumer_key="F9TnxzJ3eEK4xB1hTbIYuPERa"
consumer_secret="E18qbpu8pEiQpxRzlWRW44ZmpmGwWV2zb1Y9eZ3G8vCrrIcPZP"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="250822105-ufFJci3R3aV5IALFpmzVBTrSCVIYQDsH2Nt6k7Jn"
access_token_secret="8Hfv7AN8RnSwfM6oA9KOq8loSdWwvaJiQOcq6DwY8GB0T"

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
                row[0].strip()
                newstr = re.sub('([^a-zA-Z0-9_ # @ \'])', '', row[0])
                newstr = re.sub('(https)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(http)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(#)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(@)[a-zA-Z0-9_  # @ \%\']*', '', newstr)
                newstr = re.sub('(rt)[a-zA-Z0-9_  # @ \%\']*', '', newstr.lower())
                newstr = newstr.strip()
                if len(newstr) > 0:
                    clean.append(newstr.lower())
                    

    #write the csv    
    with open('csv\clean_tweets.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([clean])
    pass
    print "end cleanCsv"



"""
def perturbation():
    
    print "start perturbation"
   
    #I modify the tweets by including only substitution error
    
   
    
    newStr = []
    with open('csv\clean_tweets.csv', 'rb') as f:
        reader = csv.reader(f)
        #tweet_counter = 0
        for row in reader:
            row[0] = row[0].strip() #SE POI TRIMMO NEL CLEANTWEETS QUA NON SERVIREBBE PIU'
            #tweet_counter +=1
            #print "tweet numero:"
            #print tweet_counter
            number_of_errors = len(row[0])/10 # 10% della dimensione della riga
            #le = (le/10) 
            if number_of_errors > 0:
                tweet = row[0]
                #insert #le error
                for i in range(0,number_of_errors): #ciclo per il 10% dei caratteri del tweet
                    #if len(tweet) > 0:  #INUTILE QUESTO IF(?) HO GIA CONTROLLATO CHE #OFERRORS > 0 QUINDI QUESTO E' IMPLICATO
                    tweet_index = randint(0, len(tweet)-1) #indice random del tweet
                    random_letter = tweet[tweet_index] #carattere corrispondente all indice random
                    while not ground_truth.isletter(random_letter) : #ciclo finche' non scelgo una lettera
                        tweet_index = randint(0, len(tweet)-1)
                        random_letter= tweet[tweet_index]
                       
                        #random_letter = ord(random_letter) - 97 #METTI QUESTO ASSEGNAMENTO DIRETTAMNTE DENTRO L'IF (?)
                        #random_letter_ascii = len(error[ord(random_letter)-97])#num of letter's errors
                    
                    r = random.randint(0, len(error[ord(random_letter)-97]) - 1) # prendo a caso tra gli errori permessi dalla lettera in questione      
                    tweet = tweet[:tweet_index] + error[ord(random_letter)-97][r] + tweet[tweet_index+1:] #riscrivo la string con la lettera cambiata
        
                    if i == number_of_errors - 1:
                        newStr.append(tweet)
            
            
            
            else:   #se il 10% del tweet e' minore di 0
                newStr.append(row[0])
    
    #write the csv    
    with open('csv\perturbation_tweets.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerows([newStr])
    pass     

    print "end perturbation"

"""
