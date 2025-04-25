"""
File:  gene_names_from_chr21.py
Author: Liz Kiefer

Asks for user input on a gene, loops through the list of genes,
 finds it and provides the description of said gene.
"""

import argparse
import sys
import assignment4.assignment4_utils


def get_cli_args():
    """ Reads in the infile argument to a variable, confirming that it's provided. """
    parser = argparse.ArgumentParser(
        description='Asks for user input on a gene, loops through the list of genes, '
                    'finds it and provides the description of said gene.')

    parser.add_argument('-i',
                        '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to file to open',
                        required=False)
    return parser.parse_args()


def print_output(genes_dic):
    """ Loops reading user input, finding gene descriptions from that. """
    while True:
        user_input = input("Enter gene name of interest. Type quit to exit: ")
        # If user input was "quit" in any caps combination, exit
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("Thanks for querying the data.")
            sys.exit(0)
        elif user_input in genes_dic:
            print(f"{user_input} found! Here is the description: ")
            print(genes_dic[user_input]["description"])
        else:
            # Still continues looping
            print("Not a valid gene name.")
        print()


def main():  # pragma: no cover
    """ Calls the needed functions for producing output. """
    args = get_cli_args()
    infile = vars(args)["INFILE"]
    genes_dictionary = assignment4.assignment4_utils.load_dictionary(infile)
    print_output(genes_dictionary)


if __name__ == '__main__':  # pragma: no cover
    main()
