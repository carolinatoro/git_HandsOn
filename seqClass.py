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

#ensures that the sequence is valid rna or dna and then classifies it accoding to the presence of U or T
if re.search('^[ACGTU]+$', args.seq):
    # Check if the sequence contains only T (DNA) or only U (RNA)
    if 'T' in args.seq and 'U' in args.seq:
        print('Invalid sequence: contains both T and U, which is not biologically possible.')
    elif 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence is ambiguous (could be DNA or RNA)')

#if motif search is provided (since it wasn't mandatory in the arguments at the beggining of the code. if it is, it convers to uppercase here too and searches the motif in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
