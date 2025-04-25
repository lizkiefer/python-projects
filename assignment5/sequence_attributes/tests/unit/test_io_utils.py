"""
File:  test_io_utils.py
Author: Liz Kiefer

Contains unit tests for io_utils.py
"""

import pytest
from sequence_attributes import FileHandler


def test__filehandler():
    """Test for filehandler class working normally"""
    filename = "sequence_attributes/inputs/CCDS_nucleotide.current.fna"
    with FileHandler(filename, mode='r', encoding='utf-8') as in_fh:
        assert in_fh is not None


def test__filehandler_bad_file():
    """Test for filehandler class failing on bad file name"""
    bad_filename = "bad_file"
    with pytest.raises(OSError):
        with FileHandler(bad_filename, mode='r', encoding='utf-8') as in_fh:
            return in_fh


def test__filehandler_bad_mode():
    """Test for filehandler class failing on bad open mode"""
    bad_filename = "bad_file"
    with pytest.raises(ValueError):
        with FileHandler(bad_filename, mode="q", encoding='utf-8') as in_fh:
            return in_fh


def test__filehandler_bad_type():
    """Test for filehandler class failing on bad open mode type"""
    bad_filename = "bad_file"
    with pytest.raises(TypeError):
        with FileHandler(bad_filename, mode=[], encoding='utf-8') as in_fh:
            return in_fh
