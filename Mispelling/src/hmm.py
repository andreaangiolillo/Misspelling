'''
Created on 04 giu 2016

@author: Work
'''

import ground_truth
import observations_p
import tweetToCsv
import numpy
from pomegranate import *
from numpy import double
import string


nameL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


pigreco = DiscreteDistribution( { 'a': ground_truth.pigreco[0], 'b': ground_truth.pigreco[1], 'c': ground_truth.pigreco[2], 'd': ground_truth.pigreco[3], 'e': ground_truth.pigreco[4], 'f': ground_truth.pigreco[5], 'g': ground_truth.pigreco[6], 'h': ground_truth.pigreco[7],
                                 'i': ground_truth.pigreco[8], 'j': ground_truth.pigreco[9], 'k': ground_truth.pigreco[10], 'l': ground_truth.pigreco[11],'m': ground_truth.pigreco[12], 'n': ground_truth.pigreco[13], 'o': ground_truth.pigreco[14], 'p': ground_truth.pigreco[15],
                                 'q': ground_truth.pigreco[16], 'r': ground_truth.pigreco[17], 's': ground_truth.pigreco[18], 't': ground_truth.pigreco[19],'u': ground_truth.pigreco[20], 'v':ground_truth.pigreco[21], 'w': ground_truth.pigreco[22], 'x': ground_truth.pigreco[23], 'y': ground_truth.pigreco[24], 'z': ground_truth.pigreco[25]} )


model = HiddenMarkovModel("Mispelling")
def create_hmm():
    
    for i in range(0,25):#insert states
        globals()[nameL[i].strip()]= State(pigreco, name=nameL[i].strip())
        model.add_states(globals()[nameL[i].strip()])
        error = len(tweetToCsv.error_list[i])
        for n in range(0, error - 1):#insert observations
            globals()['observation_%s_%i' %(nameL[i].strip(), n )] = State(None, name=tweetToCsv.error_list[i][n].upper()+"%i"%(i))
            model.add_states(globals()['observation_%s_%i' %(nameL[i].strip(), n)])
            
    for i in range(0,25):#insert transactions
        for n in range(0,25):
            model.add_transition(globals()[nameL[i].strip()], globals()[nameL[n].strip()], ground_truth.transition_p[i][n])
            #print p_transaction1[i][n]
    for i in range(0,25):#insert observations
        error = len(tweetToCsv.error_list[i])
        for n in range(0, error - 1):
            model.add_transition(globals()[nameL[i].strip()], globals()['observation_%s_%i' %(nameL[i].strip(),n)], observations_p.obs_matrix[i][n])
   
    model.bake()
    print model 