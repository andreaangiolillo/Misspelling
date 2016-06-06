'''
Created on 30 mag 2016

@author: corrado
'''
import numpy

global TEST

TEST = "F"

def isletter(carattere):
    return ord(carattere) > 96 and ord(carattere) < 123

def iswordcorrect(parola):
    for i in range(len(parola)) :
        if not isletter(parola[i]) :
            return False
    return True

def file_to_string(file_input): 
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string


class Ground_Truth:
    
    pigreco = numpy.zeros(26)
    transition_p = numpy.zeros((26,26))
    obs_matrix = numpy.zeros(shape = (26, 26)) #dimensione esagerata, alla fine vedi se riesci a ridurla (matrice sparsa/arraylist?)
    
    def transiction(self):
        print "Start transiction"
        
        inputfile = open('csv\clean_tweets.csv')          
        word_counter = 0
        for line in inputfile : #leggo tutte le parole 
            for word in line.split() : #divido lo stream di char in string appena trovo uno spazio
                if iswordcorrect(word): #se la word contiene solo char alfabetici(escludo i # ma anche la punteggiatura)
                    if isletter(word[0]) : #DOVREBBE ESSERE INUTILE
                        self.pigreco[ord(word[0]) - 97] += 1
                        word_counter += 1
                #ora controllo le P di passare da una lettera all'altra
                    if not len(word) == 1 : #se la parola ha length almeno uguale a 2
                        for j in range(len(word)-1): #primo iteratore //faccio -1 perche incremento subito i
                            i = j + 1
                            if isletter(word[i]): #se e' falso qua itera unaltra volta
                                if isletter(word[j]): #se sono tutti e due lettere
                                    self.transition_p[ord(word[j]) - 97][ord(word[i])- 97] += 1
                                
        
        """         if not len(word) == 1 : #se la parola ha length almeno uguale a 2
                        for i in range(len(word)-1): #primo iteratore
                            i += 1 #perdoname madre por mi code loco
                            j = i-1 #j sta dietro a i
                            if isletter(word[i]): #se e' falso qua itera unaltra volta
                                if isletter(word[j]): #se sono tutti e due lettere
                                    self.transition_p[ord(word[i]) - 97][ord(word[j])- 97] += 1
                                else: #se la j non e' lettera vado indietro al massimo di uno ancora
                                    if j-1>0 and isletter(word[j-1]):
                                        self.transition_p[ord(word[i]) - 97][ord(word[j-1])- 97] += 1 """
                                        
                                        
                                        
        inputfile.close()

        if not word_counter == 0:
            for i in range(len(self.pigreco)):
                self.pigreco[i] = self.pigreco[i]/word_counter #divido ogni i dell'array per il # di parole cosi' ho la distr. di P

        for i in range(len(self.transition_p)):
            counter = 0
            for j in range(len(self.transition_p[i])):
                counter += self.transition_p[i][j]
            if not counter == 0:
                for j in range(len(self.transition_p[i])):
                    self.transition_p[i][j] = self.transition_p[i][j]/counter #round(transition_p[i][j]/(counter), 4)
    
    
        if (TEST == "T"):
            #stampa vettore pigreco
            print "vettore pigreco:"
            print self.pigreco
            print "\n" 
        
        #stampa matrice di transizioni
        print "matrice transizione:"
        for line in self.transition_p:
            print line


        print "End transiction"
        

    def observations_p(self,cleaned_tweets, perturbated_tweets):
        print "Start observations_p"

        clean_string = file_to_string(cleaned_tweets)
        pert_string = file_to_string(perturbated_tweets)
     
        if len(clean_string) == len(pert_string): #potremmo togliere questo controllo se ci fidiamo, risparimiamo 2n di computazione
            for i in range(len(clean_string)): #per ogni char controllo se sono uguali tra i due file
                if isletter(clean_string[i]): #controllo se sono lettere (se dal parse tolgo i numeri posso toglierlo)
                    self.obs_matrix[ord(clean_string[i])-97][ord(pert_string[i])-97] += 1 #altrimenti non fare nulla  
        else:
            print "ERROR: le lunghezze dei due file non coincidono"
    
        print "finito di calcolare matrice di osservazioni: "

        for i in range(len(self.obs_matrix)):
            counter = 0.0
            for j in range(len(self.obs_matrix[i])):
                counter += self.obs_matrix[i][j]
            if not counter == 0:
                for j in range(len(self.obs_matrix[i])):
                    self.obs_matrix[i][j] = float(self.obs_matrix[i][j])/counter 
                
        print "matrice di probabilita' di osservazioni: "
        for line in self.obs_matrix:
            print line

        print "End observations_p"  
