"""
File:  secondary_structure_splitter.py
Author: Liz Kiefer

Given a file name, reads it as a FASTA-formatted file and splits it into sequence and secondary
structures, printing each to a separate file.
"""

import sys
import argparse


def _verify_lists(headers, seqs):
    """ Confirms that both headers and sequences lists are the same length.
        Returns true if they're the same length, exits if not """
    if len(headers) == len(seqs):
        return True

    print("Header and Sequence lists size are different in size")
    print("Did you provide a FASTA formatted file?")
    sys.exit(1)


def get_cli_args():
    """ Reads in the infile argument to a variable, confirming that it's provided. """
    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform splitting on sequence and secondary structure')

    parser.add_argument('-i',
                        '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to file to open',
                        required=True)
    return parser.parse_args()


def get_fasta_lists(filename):
    """ Parse the FASTA file. Returns two separate lists of the headers and sequences. """
    with open(filename, mode='r', encoding='utf-8') as in_fh:
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


def output_results_to_files(headers, seqs, pdb_protein_file, pdb_ss_file):
    """ Prints the protein sequence and ss data to separate files. """
    with (open(pdb_protein_file, mode='w', encoding='utf-8') as out_pdb_protein,
          open(pdb_ss_file, mode='w', encoding='utf-8') as out_pdb_ss):
        protein_sequence = 0
        ss_sequence = 0
        for i, header in enumerate(headers):
            if header.endswith("sequence"):
                # Protein sequence found, print it
                protein_sequence += 1
                print(header, file=out_pdb_protein)
                print(seqs[i], file=out_pdb_protein)
            else:
                # SS sequence found, print it
                ss_sequence += 1
                print(header, file=out_pdb_ss)
                print(seqs[i], file=out_pdb_ss)
        print(f"Found {protein_sequence} protein sequences", file=sys.stderr)
        print(f"Found {ss_sequence} ss sequences", file=sys.stderr)


def main():  # pragma: no cover
    """ Splits a FASTA-formatted file into sequence and ss data files. """
    args = get_cli_args()
    list_headers, list_seqs = get_fasta_lists(vars(args)["INFILE"])

    output_results_to_files(list_headers, list_seqs, "pdb_protein.fasta", "pdb_ss.fasta")


if __name__ == '__main__':  # pragma: no cover
    main()
