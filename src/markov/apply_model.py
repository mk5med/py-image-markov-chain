"""
Methods related to running the model to generate the next state
"""

import random
import math


def random_key(model):
    """
    Select a random key from the model
    """
    availableKeys = list(model)
    randomKey = availableKeys[math.floor(random.random() * len(availableKeys))]
    return randomKey


def apply_model(model, ngram: str, probability: float):
    """
    Run the model and select the next state based on the `probability` argument

    Returns the next ngram of the sequence
    """

    if ngram not in model:
        ngram = random_key(model)

    # Select the available probabilities
    probabilities = model[ngram]

    # Select the first letter
    chosenNgram = probabilities[0][1]

    # Iterate through all probabilities
    for prob, val in probabilities:
        # The chosen letter is not in the current interval
        if prob <= probability:
            chosenNgram = val
        # The interval was found
        else:
            # Exit the loop
            break

    return chosenNgram
