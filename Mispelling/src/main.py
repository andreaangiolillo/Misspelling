'''
Created on 28 mag 2016

@author: Work
'''

import tweetToCsv
import ground_truth
import observations_p
import GUI
import sys
from PyQt4 import *
import sys
import observations_p
import perturbation

global TEST




if __name__ == '__main__':
    
    TEST = "T"
    """
    app = GUI.QtGui.QApplication(sys.argv)
    Mispelling = GUI.QtGui.QMainWindow()
    GUI.ui = GUI.Ui_Mispelling()
    GUI.ui.setupUi(Mispelling)
    Mispelling.show()
    sys.exit(app.exec_())
    """

   
   
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
    #to_perturbation = open('csv\clean_tweets.csv')
    perturbation.perturbate_tweets()
    #tweetToCsv.perturbation()
    ground_truth.ground_truth()
    
    clean_tweets = open('csv\clean_tweets.csv')
    perturbed_tweets = open('csv\perturbation_tweets.csv')
    
    observations_p.observations_p(clean_tweets, perturbed_tweets)