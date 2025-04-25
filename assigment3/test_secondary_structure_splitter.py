"""
File:  test_secondary_structure_splitter.py
Author: Liz Kiefer

Contains unit tests for secondary_structure_splitter.py
"""

import pytest
from secondary_structure_splitter import _verify_lists


def test__verify_lists_different_different():
    """ Check to make sure lists that are different SystemExit """

    with pytest.raises(SystemExit):
        _verify_lists([1, 2], [1, 2, 3])


def test__verify_lists_different_same():
    """  check to make sure lists that are the same return True """
    assert _verify_lists([1, 2], [1, 2]) == True
