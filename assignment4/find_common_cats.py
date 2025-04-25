"""
File:  find_common_cats.py
Author: Liz Kiefer

Given a gene data list and a gene category data list, prints each gene category and how many
genes are in it.
"""


import argparse
import assignment4.assignment4_utils
import assignment4.io_utils


def get_cli_args():
    """ Reads in the infile1 and infile2 argument to a variable. """
    parser = argparse.ArgumentParser(
        description='')

    parser.add_argument('-i1',
                        '--infile1',
                        dest='INFILE1',
                        type=str,
                        help='Path to the gene description file to open',
                        required=False)

    parser.add_argument('-i2',
                        '--infile2',
                        dest='INFILE2',
                        type=str,
                        help='Path to the gene category to open',
                        required=False)
    return parser.parse_args()


def print_output(genes_cat_dic, genes_occurrences):
    """ Prints the output of gene categories, their occurrences, and counts, to a file. """
    assignment4.io_utils.mkdir_from_infile("OUTPUT/categories.txt")
    with open("OUTPUT/categories.txt", mode='w', encoding='utf-8') as outfile:
        print("Category        Occurrence      Description", file=outfile)
        for category in sorted(genes_cat_dic.keys()):
            print(f"{category}  {genes_occurrences[category]}  {genes_cat_dic[category]}",
                  file=outfile)


def main():  # pragma: no cover
    """ Calls the needed functions for producing output. """
    args = get_cli_args()
    infile1 = vars(args)["INFILE1"]
    infile2 = vars(args)["INFILE2"]
    genes_dictionary = assignment4.assignment4_utils.load_dictionary(infile1)
    genes_category_dictionary = assignment4.assignment4_utils.load_category_dictionary(infile2)
    genes_occurrences = assignment4.assignment4_utils.count_occurrences(genes_dictionary)
    print_output(genes_category_dictionary, genes_occurrences)


if __name__ == '__main__':  # pragma: no cover
    main()
