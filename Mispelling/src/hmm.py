'''
Created on 04 giu 2016

@author: Work
'''

import numpy as np
import csv
import re 
from matplotlib.pyplot import *


import string
import numpy
from pomegranate import *
from numpy import double
from ground_truth import iswordcorrect


class Hmm:
    transition_p = []
    observations_p = []
    pigreco = []
    final_p = []
    
    nameL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    def __init__(self, tra, obs,p, f):
        self.transition_p = tra
        self.observations_p = obs
        self.pigreco = p
        self.final_p = f


    


    def create_hmm(self, error_list):
        print "matrice transizione:"
        model = HiddenMarkovModel("Mispelling")
        """pigreco1 = DiscreteDistribution( { 'a': self.pigreco[0], 'b': self.pigreco[1], 'c': self.pigreco[2], 'd': self.pigreco[3], 'e': self.pigreco[4], 'f': self.pigreco[5], 'g': self.pigreco[6], 'h': self.pigreco[7],
                                 'i': self.pigreco[8], 'j': self.pigreco[9], 'k': self.pigreco[10], 'l': self.pigreco[11],'m': self.pigreco[12], 'n': self.pigreco[13], 'o': self.pigreco[14], 'p': self.pigreco[15],
                                 'q': self.pigreco[16], 'r': self.pigreco[17], 's': self.pigreco[18], 't': self.pigreco[19],'u': self.pigreco[20], 'v':self.pigreco[21], 'w': self.pigreco[22], 'x': self.pigreco[23], 'y': self.pigreco[24], 'z': self.pigreco[25]} )
        """
        #for line in self.transition_p:
        #    print line
            
        for i in range(0,26):
            
            globals()[self.nameL[i].strip()] = State(DiscreteDistribution( { 'a': self.observations_p[i][0], 'b': self.observations_p[i][1], 'c': self.observations_p[i][2], 'd': self.observations_p[i][3], 'e': self.observations_p[i][4], 'f': self.observations_p[i][5], 'g': self.observations_p[i][6], 'h': self.observations_p[i][7],
                                 'i': self.observations_p[i][8], 'j': self.observations_p[i][9], 'k': self.observations_p[i][10], 'l': self.observations_p[i][11],'m': self.observations_p[i][12], 'n': self.observations_p[i][13], 'o': self.observations_p[i][14], 'p': self.observations_p[i][15],
                                 'q': self.observations_p[i][16], 'r': self.observations_p[i][17], 's': self.observations_p[i][18], 't': self.observations_p[i][19],
                                 'u': self.observations_p[i][20], 'v':self.observations_p[i][21], 'w': self.observations_p[i][22], 'x': self.observations_p[i][23], 
                                 'y': self.observations_p[i][24], 'z': self.observations_p[i][25]}), name = self.nameL[i].strip())

            model.add_state(globals()[self.nameL[i].strip()])
            #print self.nameL[i].strip()
            
        for i in range(0,26):
            model.add_transition(model.start, globals()[self.nameL[i].strip()], self.pigreco[i])
            
        #############################################################
        for i in range(0, 26):
            model.add_transition(globals()[self.nameL[i].strip()], model.end, self.final_p[i])
        #############################################################
            
        for i in range(0,26):#insert transactions
            for n in range(0,26):
                model.add_transition(globals()[self.nameL[i].strip()], globals()[self.nameL[n].strip()], self.transition_p[i][n])
   
        model.bake(True,None)
        
        csv_prova = open("csv\perturbation_tweets.csv")
        inferred_text = []
        prova = []
        for line in csv_prova:
            for word in line.split():
                if iswordcorrect(word) and not(word == "nan") and not(word == "inf"):
                    #print word
                    logp, path = model.viterbi(word)
                    #print "sequence: '{}' - log probability: {} - path: {}".format(''.join(word), logp, " ".join(state.name for idx, state in path))
                    for idx, state in path:
                        #print state.name
                        if (state.name != "Mispelling-start") and (state.name != "Mispelling-end"): 
                            inferred_text.append(state.name.strip())
                            #print "LUI"+state.name.strip()+"LUI"
                    inferred_text.append(" ")
                elif word == "nan":
                    inferred_text.append("man")
                elif word == "inf":
                    inferred_text.append("inc")
            prova.append(''.join(inferred_text).strip()) 
            #print string.join(inferred_text)
            inferred_text = []
        #''.join(inferred_text)
        
        with open('csv\output_tweets.csv', 'wb') as w:
            writer = csv.writer(w, delimiter= '\n')
            writer.writerows([prova])   
        
        
             
       
        
        """for i in range(0,26):#insert states
            globals()[self.nameL[i].strip()]= State(pigreco1, name=self.nameL[i].strip())
            model.add_states(globals()[self.nameL[i].strip()])
            #print self.nameL[i]
            #print i
            for n in range(0, 26):#insert observations
                if self.observations_p[i][n] > 0:
                    globals()['observation_%s_%i' %(self.nameL[i].strip(), n )] = State(pigreco1, name='observation_%s_%i' %(self.nameL[i].strip(), n))
                    model.add_states(globals()['observation_%s_%i' %(self.nameL[i].strip(), n)])
            
        for i in range(0,26):#insert transactions
            for n in range(0,26):
                model.add_transition(globals()[self.nameL[i].strip()], globals()[self.nameL[n].strip()], self.transition_p[i][n])
                #print self.nameL[i]
            for i in range(0,25):#insert observations
                error = len(error_list[i])
                for n in range(0, 26):
                    if self.observations_p[i][n] > 0:
                        model.add_transition(globals()[self.nameL[i].strip()], globals()['observation_%s_%i' %(self.nameL[i].strip(),n)], self.observations_p[i][n])
   
        model.bake(verbose=True)
        model.draw()
        print model
   """ 



    
