'''
Created on 05 giu 2016

@author: corrado
'''

"""
-valutaaione tra file perturbato e file post-correzione
-prendi i due file e scorrendo uno per uno tieni conteggio dei mismatch
-il risultato e' il rapporto tra lettere corrette e lettere non correttte
"""

#################################################################################################
##################calcolo rapporto sbagliato/corretto o originale/corretto???????????????????????
##############ovvero calcolo quante ne correggo o quante non riesco a correggerle????????????????
#################################################################################################



mismatch_counter = 0

def file_to_string(file_input): 
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string

def calculate_capabilities(original_file, post_correction_file): #POTREI PASSARE SUBITO STRINGHE???
    
    print "calcolo delle capacita' di predizione del modello:"
    
    original_string = file_to_string(original_file)
    post_string = file_to_string(post_correction_file)
    
    print len(original_string)
    print len(post_string)
    mismatch_counter = 0    
    

    print "start"
    for i in range(len(original_string)):
        
        if not (original_string[i] == post_string[i]):
            mismatch_counter += 1 
            print "original "+ original_string[i] 
            print "post "+ post_string[i]

    #print float(mismatch_counter)/len(original_string)
    
    
    """ PARTE ORIGINALE
    if len(original_string) == len(post_string):
        for i in range(len(original_string)):
            if not (original_string[i] == post_string[i]):
                mismatch_counter += 1 
    else:
        print "ERROR: le lunghezze dei due file non coincidono"     """
    
    if len(original_string) != len(post_string):
        print "ERROR: le lunghezze dei due file non coincidono" 
    
    
    