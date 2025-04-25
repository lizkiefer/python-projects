"""
File:  intersection_of_gene_names.py
Author: Liz Kiefer

Given two gene lists, finds their differences and intersection.
"""


import argparse
import assignment4.assignment4_utils
import assignment4.io_utils


def get_cli_args():
    """ Reads in the infile1 and infile2 argument to a variable. """
    parser = argparse.ArgumentParser(
        description='Provide two gene list (ignore header line), find intersection')

    parser.add_argument('-i1',
                        '--infile1',
                        dest='INFILE1',
                        type=str,
                        help='Gene list 1 to open',
                        required=False)

    parser.add_argument('-i2',
                        '--infile2',
                        dest='INFILE2',
                        type=str,
                        help='Gene list 2 to open',
                        required=False)
    return parser.parse_args()


def print_output(first_genes_dic, first_filename, second_genes_dic, second_filename):
    """ Prints the intersections and differences of two gene lists. """
    assignment4.io_utils.mkdir_from_infile("OUTPUT/intersection_output.txt")
    with open("OUTPUT/intersection_output.txt", mode='w', encoding='utf-8') as outfile:
        # Take the keys from the dictionary and use a set to make them unique
        first_genes, second_genes = assignment4.assignment4_utils.get_gene_sets(first_genes_dic,
                                                                                second_genes_dic)
        genes_intersection = first_genes.intersection(second_genes)
        print(f"Number of unique gene names in {first_filename}: "
              f"{len(first_genes.difference(second_genes))}")
        print(f"Number of unique gene names in {second_filename}: "
              f"{len(second_genes.difference(first_genes))}")
        print(f"Number of common gene symbols found: {len(genes_intersection)}")
        # Print all genes, in order, that are shared
        for gene in sorted(genes_intersection):
            print(gene, file=outfile)
        print("Output stored in OUTPUT/intersection_output.txt")


def main():  # pragma: no cover
    """ Calls the needed functions for producing output. """
    args = get_cli_args()
    infile1 = vars(args)["INFILE1"]
    infile2 = vars(args)["INFILE2"]
    if not infile1:
        infile1 = "chr21_genes.txt"
    if not infile2:
        infile2 = "HUGO_genes.txt"
    first_genes_dictionary = assignment4.assignment4_utils.load_dictionary(infile1)
    second_genes_dictionary = assignment4.assignment4_utils.load_dictionary(infile2)
    print_output(first_genes_dictionary, infile1, second_genes_dictionary, infile2)


if __name__ == '__main__':  # pragma: no cover
    main()
