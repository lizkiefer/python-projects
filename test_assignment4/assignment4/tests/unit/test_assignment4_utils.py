"""
File:  test_assignment4_utils.py
Author: Liz Kiefer

Contains unit tests for assignment4_utils.py
"""

import assignment4.assignment4_utils


def test__load_dictionary():
    """ Check to make genes dictionary can be loaded """
    infile = "chr21_genes.txt"
    genes_dict = assignment4.assignment4_utils.load_dictionary(infile)
    assert len(genes_dict) == 285


def test__load_category_dictionary():
    """ Check to make sure gene category dictionary can be loaded """
    infile = "chr21_genes_categories.txt"
    genes_cats_dict = assignment4.assignment4_utils.load_category_dictionary(infile)
    assert len(genes_cats_dict) == 10


def test__count_occurrences():
    """ Check to make sure gene category counts can be taken """
    infile = "chr21_genes.txt"
    genes_dict = assignment4.assignment4_utils.load_dictionary(infile)
    occurrences = assignment4.assignment4_utils.count_occurrences(genes_dict)
    assert len(occurrences) == 11


def test__get_gene_sets():
    """ Check that gene sets can be created from gene dictionaries """
    infile1 = "chr21_genes.txt"
    infile2 = "HUGO_genes.txt"
    first_genes_dic = assignment4.assignment4_utils.load_dictionary(infile1)
    second_genes_dic = assignment4.assignment4_utils.load_dictionary(infile2)
    first_genes, second_genes = assignment4.assignment4_utils.get_gene_sets(first_genes_dic,
                                                                            second_genes_dic)
    assert len(first_genes) == 285 and len(second_genes) == 11815
