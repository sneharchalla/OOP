#!/usr/bin/env python
import re, argparse
import itertools
import cairo 
import numpy as np

def get_args():
	parser = argparse.ArgumentParser()
	#parser.add_argument("-f", help="Input Sequence File name", required=True)
	parser.add_argument("-m", "--motif_file", help="Input Motif list", required=True)
	return parser.parse_args()

args = get_args() 
m = args.motif_file

class parse_file: 
    def __init__ (self):
        pass
    
    def parse_motif_file(self, file):
        ''' Reads a motif file which consists one motif per line, converts it into a list for use later in the script '''
        motif_list = [] #create an empty list to include all the motifs from the motif file
        with open (file, "r") as m:
            for line in m:
                line = line.strip()
                motif_list.append(line)
        print (motif_list)

   # parse_motif_file(m) 

    #def find_motif(file_handle):
       # ''' Reads an input sequence file and a motif list and finds motifs in the sequence '''
        # line_count = 0 
        # required_lines = islice (file_handle, None, 2, None) #islice returns an iterable object
        # for line in required_lines: 
            # line = line.strip()
            # if line 

    #find_motif(m)        

    # parse through the file line by line
    # compare with given motif list to find motif's
    # if motif is in the seq, store position (length - ??) and motif in dictionary(key: motif, value: pos)
    # return motif dict
    # pass

#Instantiating object for class parse_file: 
obj_m = parse_file()
#Call the function (using the object) to print the motif list: 
obj_m.parse_motif_file(m)
