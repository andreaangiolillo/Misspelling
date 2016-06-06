'''
Created on 04 giu 2016

@author: corrado
'''

import numpy
from ground_truth import isletter

obs_matrix = numpy.zeros(shape = (26, 26)) #dimensione esagerata, alla fine vedi se riesci a ridurla (matrice sparsa/arraylist?)
"""
def count_legth(file_input): #toglibile
    c = 0
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                c += 1
    return c
"""
def file_to_string(file_input): 
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string

def observations_p(cleaned_tweets, perturbated_tweets):
    print "calcolo probabilita' delle osservazioni"


    #PROVA POI SE RIESCI A FARLO CON  UNA STINGA UNICA
    clean_string = file_to_string(cleaned_tweets)
    pert_string = file_to_string(perturbated_tweets)
    #l_clean = count_legth(cleaned_tweets)
    #l_pert = count_legth(perturbated_tweets)
    #print "file in stringa"
    #print string_clean
    #print string_pert
     
    if len(clean_string) == len(pert_string): #potremmo togliere questo controllo se ci fidiamo, risparimiamo 2n di computazione
        for i in range(len(clean_string)): #per ogni char controllo se sono uguali tra i due file
            if isletter(clean_string[i]): #controllo se sono lettere (se dal parse tolgo i numeri posso toglierlo)
                obs_matrix[ord(clean_string[i])-97][ord(pert_string[i])-97] += 1 #altrimenti non fare nulla
            """
            if clean_string[i] == pert_string[i]: #se coincidono incremento sulla diagonale
                if ground_truth.is_letter(clean_string): #controllo se sono lettere (se dal parse tolgo i numeri posso toglierlo)
                    obs_matrix[ord(clean_string)-97][ord(pert_string)-97] += 1 #altrimenti non fare nulla
            else: #se non coincidono incrementa la colonna corrispondente
                obs_matrix[ord(clean)] """  
    else:
        print "ERROR: le lunghezze dei due file non coincidono"
    
    
    print "finito di calcolare matrice di osservazioni: "
    for line in obs_matrix:
        print line

    for i in range(len(obs_matrix)):
        counter = 0.0
        for j in range(len(obs_matrix[i])):
            counter += obs_matrix[i][j]
        if not counter == 0:
            for j in range(len(obs_matrix[i])):
                obs_matrix[i][j] = float(obs_matrix[i][j])/counter #round(transition_p[i][j]/(counter), 4)
                
    print "matrice di probabilita' di osservazioni: "
    for line in obs_matrix:
        print line
"""
    #############
    if len(clean_tweets) == len(perturbate_tweets) :
        for i in range(0, len(clean_tweets)-1):
            if clean_tweets[i] == perturbate_tweets[i]:
                #incrementa obs_matrix[i][i]
            else:
                #calcola che lettera e' e aggiorna obs_matrix[i][altra lettera]
        
        for row in range(len(obs_matrix)):
            c = 0
            for column in range(len(obs_matrix[row])):
                c += obs_matrix[row][column]
            if not c == 0:
                for column in range(len(obs_matrix[row])):
                    obs_matrix[row][column] = obs_matrix[row][column]/c
                
                
        for i in range(len(transition_p)):
            counter = 0
            for j in range(len(transition_p[i])):
                counter += transition_p[i][j]
            if not counter == 0:
                for j in range(len(transition_p[i])):
                    transition_p[i][j] = transition_p[i][j]/counter #round(transition_p[i][j]/(counter), 4)
"""