'''
Created on 28 mag 2016

@author: Work
'''

import tweetToCsv
import ground_truth

global TEST




if __name__ == '__main__':
    
    TEST = "T"
    
    #download tweet and put all in csv
    
    """
    tweetToCsv.get_all_tweets("BBCBreaking")
    tweetToCsv.get_all_tweets("POTUS")
    tweetToCsv.get_all_tweets("nytimes")
    tweetToCsv.get_all_tweets("WSJPolitics")
    tweetToCsv.get_all_tweets("NBA")
    tweetToCsv.get_all_tweets("SkyFootball")
    tweetToCsv.get_all_tweets("Pontifex")  
    tweetToCsv.get_all_tweets("WWF")
    tweetToCsv.get_all_tweets("WSJ")
    tweetToCsv.get_all_tweets("UN")
    """
    #tweetToCsv.cleanCsv()
    #tweetToCsv.perturbation()
    ground_truth.ground_truth()