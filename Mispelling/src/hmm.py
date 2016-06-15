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
from ground_truth import iswordcorrect, isletter


class Hmm:
    transition_p = []
    observations_p = []
    pigreco = []
    final_p = []
    model = ""
    
    nameL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    def __init__(self, tra, obs,p, f):
        self.transition_p = tra
        self.observations_p = obs
        self.pigreco = p
        self.final_p = f


    def create_hmm(self, error_list):
        
        self.model = HiddenMarkovModel("Mispelling")
            
        for i in range(0,26):
            
            globals()[self.nameL[i].strip()] = State(DiscreteDistribution( { 'a': self.observations_p[i][0], 'b': self.observations_p[i][1], 'c': self.observations_p[i][2], 'd': self.observations_p[i][3], 'e': self.observations_p[i][4], 'f': self.observations_p[i][5], 'g': self.observations_p[i][6], 'h': self.observations_p[i][7],
                                 'i': self.observations_p[i][8], 'j': self.observations_p[i][9], 'k': self.observations_p[i][10], 'l': self.observations_p[i][11],'m': self.observations_p[i][12], 'n': self.observations_p[i][13], 'o': self.observations_p[i][14], 'p': self.observations_p[i][15],
                                 'q': self.observations_p[i][16], 'r': self.observations_p[i][17], 's': self.observations_p[i][18], 't': self.observations_p[i][19],
                                 'u': self.observations_p[i][20], 'v':self.observations_p[i][21], 'w': self.observations_p[i][22], 'x': self.observations_p[i][23], 
                                 'y': self.observations_p[i][24], 'z': self.observations_p[i][25]}), name = self.nameL[i].strip())

            self.model.add_state(globals()[self.nameL[i].strip()])
            #print self.nameL[i].strip()
            
        for i in range(0,26):
            self.model.add_transition(self.model.start, globals()[self.nameL[i].strip()], self.pigreco[i])
            
        for i in range(0, 26):
            self.model.add_transition(globals()[self.nameL[i].strip()], self.model.end, self.final_p[i])
            
        for i in range(0,26):#insert transactions
            for n in range(0,26):
                self.model.add_transition(globals()[self.nameL[i].strip()], globals()[self.nameL[n].strip()], self.transition_p[i][n])
   
        self.model.bake(True,None)
        
        csv_prova = open("csv\perturbation_tweets.csv")
        inferred_text = []
        prova = []
        for line in csv_prova:
            for word in line.split():
                if iswordcorrect(word) and not(word == "nan") and not(word == "inf"):
                    #print word
                    logp, path = self.model.viterbi(word)  
                    for idx, state in path:
                        #print state.name
                        if (state.name != "Mispelling-start") and (state.name != "Mispelling-end"): 
                            inferred_text.append(state.name.strip())
                    inferred_text.append(" ")
                elif word == "nan":
                    inferred_text.append("man ")
                elif word == "inf":
                    inferred_text.append("inc ")
            prova.append(''.join(inferred_text).strip()) 
            inferred_text = []
        
        with open('csv\output_tweets.csv', 'wb') as w:
            writer = csv.writer(w, delimiter= '\n')
            writer.writerows([prova])   
           
    txt = []
    out = ""
    zuzzu = ""
    def correct_from_input(self, input_text):
        print input_text
        self.zuzzu = ''.join(str(input_text).lower())
        self.txt = []
        for word in self.zuzzu.split():
            if (word == "nan"):
                word = "man"
            if (word == "inf"):
                word = "inc"
            self.correct_word(word)
        self.out = ''.join(self.txt).strip()
        return self.out

   
    def correct_word(self, word):
        for i in range(len(word)):
            if not isletter(word[i]):
                if not len(word[:i]) == 0:     
                    logp, path = self.model.viterbi(word[:i])
                    for idx, state in path:
                        if (state.name != "Mispelling-start") and (state.name != "Mispelling-end"):
                            self.txt.append(state.name.strip())
                    self.txt.append(word[i])
                if len(word[i+1:]) == 0:
                    self.txt.append(' ')
                else:
                    self.correct_word(word[i+1:])
                return  
        if not len(word) == 0:
            logp, path = self.model.viterbi(word)
            for idx, state in path:
                if (state.name != "Mispelling-start") and (state.name != "Mispelling-end"): 
                    self.txt.append(state.name.strip())
            self.txt.append(" ")
            
            
            
            
            
            