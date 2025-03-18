#create and modify a python script that computes, given a DNA or RNA sequence, the percentage of each nucleotide

#start by deciding if the sequence is DNA or RNA (used previous code used in lesson)

#!/usr/bin/env python

#import required modules for script to run
import sys, re
from argparse import ArgumentParser

#argument parser helps manage command line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
#\-\-seq handles the string input sequence 
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
#motif to search within the sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

#handles an error if the script is run without arguments, stops and exits with status 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

#user provided arguments are stored in args
args = parser.parse_args()

#converts the sequence to uppercase to handle lowercase not being recognised
args.seq = args.seq.upper()                 # Note we just added this line

#ensures that the sequence is valid rna or dna and then classifies it accoding to the presence of U or T. Based on this classification, it computes percentage of each nucleotide
if re.search('^[ACGTU]+$', args.seq):

    counts = {}
    tot_nucleo = len (args.seq)
    
    # Check if the sequence contains only T (DNA) or only U (RNA)
    if 'T' in args.seq and 'U' in args.seq:
        print('Invalid sequence: contains both T and U, which is not biologically possible.')
  
    elif 'T' in args.seq: # if DNA
        print('The sequence is DNA')
        #initialize the counts
        counts = {'A':0, 'T':0, 'C':0, 'G':0}
          
    elif 'U' in args.seq: # if RNA
        print('The sequence is RNA')
        #initialize the counts
        counts = {'A':0, 'U':0, 'C':0, 'G':0}

    else:
        print('The sequence is ambiguous (could be DNA or RNA)')

    #now count nucleotide percentages
    for nucleo in args.seq:
      if nucleo in counts:
        counts[nucleo] = += 1
    
    print('\nNucleotide percentages:')
    for nucleotide, count in counts.items():
      percentage = (count/tot_nucleo)*100
      print(f"{nucleotide}: {percentage:.2f}%")

#if motif search is provided (since it wasn't mandatory in the arguments at the beggining of the code. if it is, it convers to uppercase here too and searches the motif in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
