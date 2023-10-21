def create_model(wordCounts, sampleCount):
    model = {}
    for ngram in sampleCount:
        samples = sampleCount[ngram]

        probabilities = []
        # Calculate the probabilities
        for key in wordCounts[ngram]:
            probability = wordCounts[ngram][key] / samples
            probabilities.append((probability, key))

        # Order the probabilities from low to high
        probabilities.sort(key=lambda x: x[0])

        summedProbability = []
        _prob = 0

        # Create a new list where the set of all
        # probabilities is in the interval of 0 to 1
        for p, val in probabilities:
            _prob += p
            summedProbability.append((_prob, val))

        model[ngram] = summedProbability

    return model
