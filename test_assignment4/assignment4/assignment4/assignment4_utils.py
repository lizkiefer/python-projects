"""
File:  assignment4_utils.py
Author: Liz Kiefer

Contains utility functions for assignment 4
"""


def load_dictionary(infile):
    """ Reads a gene file and loads available data into a dictionary. """
    if not infile:
        infile = "chr21_genes.txt"
    with open(infile, mode='r', encoding='utf-8') as in_fh:
        genes_dic = {}
        # Loop through each line in the file
        # The first line is skipped because it is header information
        next(in_fh)
        for line in in_fh:
            gene_data = line.split('\t')
            gene_dic = {}
            if len(gene_data) > 1:
                gene_dic["description"] = gene_data[1]
            if len(gene_data) > 2:
                # The entry needs to be stripped to remove the newline character
                gene_dic["category"] = gene_data[2].strip()
            genes_dic[gene_data[0]] = gene_dic
        return genes_dic


def load_category_dictionary(infile):
    """ Loads a set of gene categories and data into a dictionary. """
    if not infile:
        infile = "chr21_genes_categories.txt"
    with open(infile, mode='r', encoding='utf-8') as in_fh:
        genes_cat_dic = {}
        # Loop through each line in the file
        for line in in_fh:
            gene_data = line.split('\t')
            # Add a new genes category dictionary entry
            # With the key being the gene name, and the value being the description
            genes_cat_dic[gene_data[0]] = gene_data[1]
        return genes_cat_dic


def count_occurrences(genes_dic):
    """ Counts how many times a category appears in a gene dictionary. """
    genes_occurrences = {}
    for gene in genes_dic:
        if genes_dic[gene]["category"] in genes_occurrences:
            # Increment the existing entry
            genes_occurrences[genes_dic[gene]["category"]] += 1
        else:
            # Add a new entry starting at 1
            genes_occurrences[genes_dic[gene]["category"]] = 1
    return genes_occurrences


def get_gene_sets(first_genes_dic, second_genes_dic):
    """ Receives two gene dictionaries and reduces them to sets of their keys. """
    first_genes = set(first_genes_dic.keys())
    second_genes = set(second_genes_dic.keys())

    return first_genes, second_genes
