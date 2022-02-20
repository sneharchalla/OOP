#!/usr/bin/env python
import re, argparse
import itertools
import cairo 
import numpy as np

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--fasta_file", help="Input Sequence File", required=True)
	parser.add_argument("-m", "--motif_file", help="Input Motif list", required=True)
	return parser.parse_args()

args = get_args() 
m = args.motif_file
f = args.fasta_file

class parse_file: 
	
	#Constructor
	def __init__ (self):
		pass
    
	def parse_motif_file(self, motif_file):
		''' Reads a motif file which consists one motif per line, converts it into a list for use later in the script '''
		motif_list = [] #create an empty list to include all the motifs from the motif file
		with open (motif_file, "r") as m:
			for line in m:
				line = line.strip()
				motif_list.append(line)
		return motif_list

	#parse_motif_file(m) 

	def find_motif(self, motif_list, seq_file):
		#''' Takes the sequence file and motif list as input and finds motifs in the sequence from the sequence file '''
		line_count = 0 
		header_list = []
		motif_dict = [] # key = motif, value = start and end positions of motif, chrm number, gene name
		with open (seq_file, "r") as f:
			for line in f: 
				line = line.strip()
				print(line)
				if line[0].startswith(">"):
					print (line[0])
					print("This is a header line")
					header_list.append(line)
					line_count += 1
				else: 
					if line_count % 2 == 0:
						#print(line)
						self.parse_motif_file(m) #calling function parse_motif_file to get the output of that function which is the motif list.
						#Now loop through each line in the seq file to find motifs from list and extract start and end position of the motif and add the motif, its positions to a dictionary. 
						for position in range(len(line)):
							for i in motif_list: 
								if line[position:].startswith(i):
									motif_dict.setdefault(i, [])
									#calculate start and end pos of motif
									s_pos = position + 1
									e_pos = s_pos + len(i)
									#add to motif_dict
									motif_dict[i].append(s_pos)
									motif_dict[i].append(e_pos)
								
						
		print (header_list)
		print (motif_dict)

    #find_motif(m)        
	def amb_motif(self, motif_list):
			#''' Parses the motif list and identifies ambiguous motifs'''					
		new_list = []
		amb_motif_dict = {R:["A","G"], Y: ["C", "U"] ,S: ["C", "G"] , W: ["A", "U"] , K: ["G", "U"] , M:["A", "C"] , B: ["C", "G", "U"] , D: ["A", "G", "U"] , H: ["A", "C", "U"] , V: ["A", "C", "G"] , N: ["A", "C", "G"], "U" }
			# TODO # : You have to account for upper and lowercase ambiguous 
		for i in motif_list: 
			if i in amb_motif_dict.keys():
				new_list.append(amb_motif_dict.get(i))
		return new_list

		#regex_obj = re.compile("Py...n")
		#for i in range(10000):
			#match = regex_obj.search("Python is great" + str(i))
		#	print(match)
		
			pass

	def find_preslice(self, seq_file):
		#''' Finds the exons and introns in the sequence file '''
		exon = re.search('[A-Z]+', line).span()
		intron = re.search('[a-z]+', line).span()
    
class draw_fig: 
	
	#Constructor
	def __init__ (self):
		pass
    
	def draw_rectangle(self):
		pass
	
	def draw_lines(self):
		#'''Draw both vertical and horizontal lines '''
		pass

#Instantiating object for class parse_file: 
obj_m = parse_file()

#Call the function "parse_motif_file" (using the object) to print the motif list: 
obj_m.parse_motif_file(m)
#Call the function "find_motif" (using the object) to print the header list: 
obj_m.find_motif(list, f)



