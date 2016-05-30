'''
Created on 28 mag 2016

@author: Work
'''
import tweetToCsv
import ground_truth

if __name__ == '__main__':
    
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
    tweetToCsv.cleanCsv()
    ground_truth.ground_trut()