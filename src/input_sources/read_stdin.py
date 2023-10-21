"""
Methods for reading STDIN input from the user
"""

import sys


def read_all_input():
    """
    Reads all lines from STDIN
    """
    return " ".join(sys.stdin.readlines())
