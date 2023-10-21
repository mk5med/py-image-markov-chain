import random
import math


def random_key(model):
    availableKeys = [key for key in model]
    randomKey = availableKeys[math.floor(random.random() * len(availableKeys))]
    return randomKey


def apply_model(model, letter: str, probability: float):
    if letter not in model:
        letter = random_key(model)
    probabilities = model[letter]
    chosenLetter = probabilities[0][1]

    for prob, val in probabilities:
        if prob <= probability:
            chosenLetter = val
        else:
            break

    return chosenLetter
