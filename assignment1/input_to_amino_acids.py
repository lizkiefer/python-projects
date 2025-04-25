"""

File:  input_to_amino_acids.py
Author: Liz Kiefer

Given a sequence name, a sequence length, and a decoded protein length,
calculate the average weight of the protein sequence.
Exit if the protein length is not divisible by 3.
"""

import sys

name = input('Please enter a name for the DNA sequence: ')
print('Your sequence name is: ' + name)
seqLength = float(input('Please enter the length of the sequence: '))
if seqLength % 3 == 0:
    print('The length of the DNA sequence is: ' + str(seqLength))
    proLength = seqLength/3
    print('The length of the decoded protein is: ' + str(proLength))
    print('The average weight of the protein sequence is: ' + str((proLength * 110)/1000))
else:
    print('Error: the DNA sequence is not a multiple of 3')
    sys.exit(1)
