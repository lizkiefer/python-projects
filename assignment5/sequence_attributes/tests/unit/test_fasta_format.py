"""
File:  test_fasta_format.py
Author: Liz Kiefer

Contains unit tests for fasta_format.py
"""

import pytest
from sequence_attributes import get_fasta_lists, _verify_lists  # pylint: disable=W0212


def test__verify_lists_different_different():
    """ check to make sure lists that are different SystemExit """
    with pytest.raises(SystemExit):
        _verify_lists([1, 2], [1, 2, 3])


def test__verify_lists_different_same():
    """ Check to make sure lists that are the same return True """
    assert _verify_lists([1, 2], [1, 2]) is True


def test__get_fasta_lists():
    """ Check to make sure given FASTA file can be loaded """
    filename = "sequence_attributes/inputs/CCDS_nucleotide.current.fna"
    headers, seqs = get_fasta_lists(filename)
    assert len(headers) == len(seqs) and len(headers) != 0
