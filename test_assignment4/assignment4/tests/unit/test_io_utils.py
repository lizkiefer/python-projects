"""
File:  test_io_utils.py
Author: Liz Kiefer

Contains unit tests for io_utils.py
"""

import os
import pytest
import assignment4.io_utils


def test__mkdir_from_infile():
    """ Ensure a FileNotFoundError is raised if no directory is found """
    file_name = "OUTPUT/testfile.txt"
    assignment4.io_utils.mkdir_from_infile(file_name)
    assert os.path.isdir(os.path.dirname(file_name))


def test__mkdir_from_infile_bad_file():
    """ Ensure a FileNotFoundError is raised if no directory is found """
    bad_file = "nofile"
    with pytest.raises(FileNotFoundError):
        assignment4.io_utils.mkdir_from_infile(bad_file)
