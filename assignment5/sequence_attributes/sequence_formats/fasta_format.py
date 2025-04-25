"""
File:  fasta_format.py
Author: Liz Kiefer

Contains utility functions for processing FASTA-formatted files
"""

import sys
from typing import Tuple
from sequence_attributes.utils.io_utils import FileHandler


def _verify_lists(headers: list = None, seqs: list = None):
    """ Confirms that both headers and sequences lists are the same length.
        Returns true if they're the same length, exits if not """
    if len(headers) == len(seqs):
        return True

    print("Header and Sequence lists size are different in size")
    print("Did you provide a FASTA formatted file?")
    sys.exit(1)


def get_fasta_lists(infile: str = None) -> Tuple[list, list]:
    """ Parse the FASTA file. Returns two separate lists of the headers and sequences. """
    with FileHandler(infile, mode='r', encoding='utf-8') as in_fh:
        headers = []
        seqs = []
        current_sequence = ""
        # Loop through each line in the file
        for line in in_fh:
            if line.startswith('>'):
                # Header line found, add it to headers list
                headers.append(line.rstrip('\n'))
                # If sequence is found add it to sequences list
                if current_sequence != "":
                    seqs.append(current_sequence)
                    current_sequence = ""
            else:
                # Sequence found add it to current sequence list
                current_sequence += line.rstrip('\n')
        if current_sequence != "":
            # Add the final sequence to the list
            seqs.append(current_sequence)

        # check to make sure data looks good. Note, no return value, so no assignment
        _verify_lists(headers, seqs)

        return headers, seqs
