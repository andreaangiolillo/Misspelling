'''
Created on 05 giu 2016

@author: corrado
'''
#import csv #usato solo nel debugging

mismatch_counter = 0

def file_to_string(file_input): 
    file_string = ""
    for line in file_input:
        for word in line.split():
            for i in range(len(word)-1):
                file_string += word[i]
    return file_string

def calculate_capabilities(original_file, post_correction_file, gui, parola = "Before: "):
    
    original_string = file_to_string(original_file)
    post_string = file_to_string(post_correction_file)
    
    mismatch_counter = 0    
    
    if len(original_string) == len(post_string):
        for i in range(len(original_string)):
            if not (original_string[i] == post_string[i]):
                mismatch_counter += 1
        print gui.textBrowser.append("Errors "+ parola+ "\n" + str( float(mismatch_counter)/len(original_string)))
    else:
        print gui.textBrowser.append("ERROR: le lunghezze dei due file non coincidono")    
        
        
        
        
        
        
        
        
        
    """                       ######### PER TESTING #########
    
    with open('csv\clean_tweets.csv', 'rb') as f1, open('csv\output_tweets.csv', 'rb') as f2:
        rdr1 = csv.reader(f1)
        rdr2 = csv.reader(f2)
        c = 1
        for file1_line in rdr1:
            file2_line = rdr2.next()
            c += 1
            #print file1_line[0]
            #print file2_line[0]
            if not (len(file1_line[0]) == len(file2_line[0])):
                print "righe diverse cazzo vi ho gamato:"
                print file1_line
                print file2_line
                print "linea "
                print c
    """