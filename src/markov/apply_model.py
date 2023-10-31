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
    probabilityIntervals = model[ngram]

    chosenNgram = None

    # Iterate through all probabilities
    for ngramProbability, ngramVal in probabilityIntervals:
        # The probability is in the current probability interval
        if probability <= ngramProbability:
            chosenNgram = ngramVal
            break

    return chosenNgram
