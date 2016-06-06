'''
Created on 28 mag 2016

@author: Work
'''

from tweetToCsv import TweetToCsv
from ground_truth import Ground_Truth
from hmm import Hmm

import GUI
import sys
from PyQt4 import *
import sys





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

    csv = TweetToCsv()
    esteem = Ground_Truth()
    #download tweet and put all in csv
    
    """csv.get_all_tweets("POTUS")
    csv.get_all_tweets("BBCBreaking")
    
    csv.get_all_tweets("nytimes")
    csv.get_all_tweets("WSJPolitics")
    csv.get_all_tweets("NBA")
    csv.get_all_tweets("SkyFootball")
    csv.get_all_tweets("Pontifex")  
    csv.get_all_tweets("WWF")
    csv.get_all_tweets("WSJ")
    csv.get_all_tweets("UN")"""
   
    csv.cleanCsv()
    csv.perturbate_tweets()
    
    esteem.transiction()
    clean_tweets = open('csv\clean_tweets.csv')
    perturbed_tweets = open('csv\perturbation_tweets.csv')
    esteem.observations_p(clean_tweets, perturbed_tweets)
    
    hmm = Hmm(esteem.transition_p, esteem.obs_matrix, esteem.pigreco )
    hmm.create_hmm(csv.error_list)
    

  