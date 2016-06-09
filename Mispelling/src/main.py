'''
Created on 28 mag 2016

@author: Work
'''

from tweetToCsv import TweetToCsv
from ground_truth import Ground_Truth
from hmm import Hmm

import gui22
import sys
from PyQt4 import *
import sys
import prediction_capabilities
import csv
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
    
    """
    csv.get_all_tweets("UKLabour")
    csv.get_all_tweets("Conservatives")
    csv.get_all_tweets("David_Cameron")
    csv.get_all_tweets("MayorofLondon")
    csv.get_all_tweets("UniofOxford")
    csv.get_all_tweets("Cambridge_Uni")
    csv.get_all_tweets("tcddublin")
    """
   
    csv.cleanCsv()
    csv.perturbate_tweets()
   
    esteem.transiction()
    clean_tweets = open('csv\clean_tweets.csv')
    perturbed_tweets = open('csv\perturbation_tweets.csv')
    esteem.observations_p(clean_tweets, perturbed_tweets)
    
    
    
    
    hmm = Hmm(esteem.transition_p, esteem.obs_matrix, esteem.pigreco, esteem.final_p )
    hmm.create_hmm(csv.error_list)


    print "################################################################"
    print "DIFFERENZA TRA ORIGINALI"
    clean_tweets = open('csv\clean_tweets.csv')
    perturbed_tweets = open('csv\perturbation_tweets.csv')
    prediction_capabilities.calculate_capabilities(clean_tweets, perturbed_tweets)
    
    print "################################################################"
    print "DIFFERENZA FINALE"
    clean_tweets = open('csv\clean_tweets.csv')
    output_tweets = open('csv\output_tweets.csv')
    prediction_capabilities.calculate_capabilities(clean_tweets, output_tweets)
       
    ##############################################################################################
    
    
"""
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = gui22.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

 """   
    
    
    

