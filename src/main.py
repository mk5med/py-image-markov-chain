"""
Main entrypoint for the program
"""

import random
import argparse

# sys.path.insert(0, os.getcwd())

from img_process.img2text import img2text
from img_process.text2img import text2img
from input_sources.read_stdin import read_all_input
from markov.apply_model import apply_model, random_key
from markov.setup_model import setup_model


def create_string(model, initial: str, length: int, separator=""):
    lastLetter = initial
    outArr = [initial]

    # Loop length-1 times because the first letter is already set
    for i in range(length - 1):
        # Apply the model to get the next letter
        newLetter = apply_model(model, lastLetter, random.random())

        # Append the letter to the output
        outArr.append(newLetter)

        lastLetter = newLetter

    return separator.join(outArr)


def process_text():
    """
    Process input from STDIN
    Generates real-looking text
    """
    text = read_all_input()
    model = setup_model(text)

    return create_string(model, random_key(model), 1500, " ")


def process_img(imagePath: str):
    """
    Process an image passed as an argument
    Generates 2D textures
    """
    (masks, maskHash) = img2text(imagePath)

    model = setup_model(" ".join(maskHash))

    # Create sample images
    imgs = []

    for i in range(4):
        output = create_string(model, random_key(model), 1500, " ")
        img = text2img(output, masks)
        imgs.append(img)
        img.show()
    return imgs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="PY-Markov Chain",
    )
    parser.add_argument("-t", "--text")
    parser.add_argument("-i", "--image")

    args = parser.parse_args()

    if args.text:
        print(process_text())
    elif args.image:
        process_img(args.image)
