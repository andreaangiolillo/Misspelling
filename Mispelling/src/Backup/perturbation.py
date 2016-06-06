'''

Created on 04 giu 2016

@author: corrado
'''
import random
import csv
from ground_truth import isletter
import tweetToCsv
from numpy.random.mtrand import randint
from tweetToCsv import error_list


def perturbate_tweets(): 
    riscrittura = []
    with open('csv\clean_tweets.csv', 'rb') as r:
        reader = csv.reader(r)
        for line in reader:
            tweet = line[0]
            for i in range(len(tweet)):
                if isletter(tweet[i]):
                    r = random.random()
                    if r < 0.1:
                        r_index = random.randint(0, len(error_list[ord(tweet[i])-97]) - 1)
                        tweet = tweet[:i] + tweetToCsv.error_list[ord(tweet[i])-97][r_index] + tweet[i+1:]
                if i == len(tweet)-1:
                    riscrittura.append(tweet)
     
    with open('csv\perturbation_tweets.csv', 'wb') as w:
        writer = csv.writer(w, delimiter='\n')
        writer.writerows([riscrittura])               
                    
    print "finito"