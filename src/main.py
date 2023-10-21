import random
import sys
import os

# sys.path.insert(0, os.getcwd())

from img_process.text2img import text2img
from input_sources.get_input_from_file import get_input_from_file
from input_sources.read_all_input import read_all_input
from markov.apply_model import apply_model, random_key
from markov.setup_model import setup_model


def create_string(model, initial: str, length: int, separator=""):
    lastLetter = initial
    outStr = initial + separator
    for i in range(length - 1):
        newLetter = apply_model(model, lastLetter, random.random())
        outStr += newLetter + separator
        lastLetter = newLetter

    return outStr


def process_text():
    """
    Process input from STDIN
    Generates real-looking text
    """
    text = read_all_input()
    model = setup_model(text)

    return create_string(model, random_key(model), 1500, " ")


def process_img():
    """
    Process an image passed as an argument
    Generates 2D textures
    """
    text = get_input_from_file()
    model = setup_model(text)

    # Create sample images
    imgs = []
    for i in range(4):
        output = create_string(model, random_key(model), 1500, " ")
        print(output)
        img = text2img(output)
        imgs.append(img)
        img.show()
    return imgs


if __name__ == "__main__":
    # processTextInput()
    process_img()
