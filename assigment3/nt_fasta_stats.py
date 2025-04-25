"""
File:  nt_fasta_stats.py
Author: Liz Kiefer

Given a file name, reads it as a FASTA-formatted file and prints statistics to an output file
about the sequences present in the file.
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


def _get_num_nucleotides(nucleotide, sequence):
    """ Given a nucleotide (A, T, C, G, or N), returns the number of that nucleotide
    in a given sequence. """
    allowed_nucleotides = ['A', 'T', 'C', 'G', 'N']
    if nucleotide not in allowed_nucleotides:
        sys.exit("Did not code this condition")
    return sequence.count(nucleotide)


def _get_ncbi_accession(header):
    """ Returns the accession name for a sequence header. """
    return header.split()[0].lstrip(">")


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

    parser.add_argument('-o',
                        '--outfile',
                        dest='OUTFILE',
                        type=str,
                        help='Path to file to write',
                        required=True)
    return parser.parse_args()


def get_fasta_lists(filename):
    """ Parse the FASTA file. Returns two separate lists of the headers and sequences. """
    with open(filename, mode='r', encoding='utf-8') as in_fh:
        headers = []sp
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


def print_sequence_stats(headers, seqs, outfile_name):
    """ Prints the protein sequence statistics to an outfile. """
    with open(outfile_name, mode='w', encoding='utf-8') as out_file:
        print("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%", file=out_file)
        for i, header in enumerate(headers):
            # Build statistics for this sequence
            accession_nt = _get_ncbi_accession(header)
            a_nt = _get_num_nucleotides('A', seqs[i])
            g_nt = _get_num_nucleotides('G', seqs[i])
            c_nt = _get_num_nucleotides('C', seqs[i])
            t_nt = _get_num_nucleotides('T', seqs[i])
            n_nt = _get_num_nucleotides('N', seqs[i])
            len_nt = len(seqs[i])
            gc_nt = ((g_nt + c_nt) / len_nt) * 100
            print(f"{i + 1}\t{accession_nt}\t{a_nt}\t{g_nt}\t{c_nt}\t{t_nt}\t{n_nt}\t{len_nt}"
                  f"\t{gc_nt:.1f}", file=out_file)


def main():  # pragma: no cover
    """ Prints statistics about a FASTA file to an output file. """
    args = get_cli_args()
    list_headers, list_seqs = get_fasta_lists(vars(args)["INFILE"])
    outfile_name = vars(args)["OUTFILE"]

    # process the sequences and print out the data
    print_sequence_stats(list_headers, list_seqs, outfile_name)


if __name__ == '__main__':  # pragma: no cover
    main()
