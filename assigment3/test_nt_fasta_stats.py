"""
File:  test_nt_fasta_stats.py
Author: Liz Kiefer

Contains unit tests for nt_fasta_stats.py
"""

import pytest
from nt_fasta_stats import _get_num_nucleotides, _verify_lists


def test__verify_lists_different_different():
    """ check to make sure lists that are different SystemExit """

    with pytest.raises(SystemExit):
        _verify_lists([1, 2], [1, 2, 3])


def test__verify_lists_different_same():
    """ Check to make sure lists that are the same return True """
    assert _verify_lists([1, 2], [1, 2]) == True


def test__get_num_nucleotides():
    """ Check to make sure imvalid nucleotide returns sys exit """

    with pytest.raises(SystemExit):
        _get_num_nucleotides("B", "L")
