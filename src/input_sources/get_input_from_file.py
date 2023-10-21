import sys
from img_process.img2text import img2text


def get_input_from_file():
    if len(sys.argv) < 1:
        print("This program requires a file name")

    return img2text(sys.argv[1])
