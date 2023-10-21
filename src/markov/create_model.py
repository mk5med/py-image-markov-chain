"""
Methods for creating models
"""

import typing


def create_model(
    ngramCounts: typing.Dict[str, typing.Dict[str, int]],
    sampleCount: typing.Dict[str, int],
):
    """
    Given ngram count and sample count dictionaries this generates
    a model that defines the probability of navigating to an ngram from another ngram
    """
    model = {}
    for ngram in sampleCount:
        samples = sampleCount[ngram]

        probabilities = []

        # Calculate the probabilities
        for nextNgram in ngramCounts[ngram]:
            probabilityForNextNgram = ngramCounts[ngram][nextNgram] / samples
            probabilities.append((probabilityForNextNgram, nextNgram))

        # Order the probabilities from low to high
        probabilities.sort(key=lambda x: x[0])

        summedProbability = []
        _prob = 0.0

        # Create a new list where the set of all
        # probabilities is in the interval of 0 to 1
        for p, val in probabilities:
            _prob += p
            summedProbability.append((_prob, val))

        # Save the relationship
        model[ngram] = summedProbability

    return model
