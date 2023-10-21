"""
Methods for reading from files
"""

import sys
from img_process.img2text import img2text


def get_input_from_img():
    """
    Reads input from an image file and encodes it as text
    """
    if len(sys.argv) < 1:
        print("This program requires a file name")

    return img2text(sys.argv[1])
