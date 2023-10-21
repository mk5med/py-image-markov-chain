"""
Methods for calculating the statistics of text
Used to generate a finite state machine with `create_model`
"""


def calculate_statistics(text: str):
    sampleCount = {}
    ngramCount = {}
    ngrams = text.split(" ")

    # Start from index 1 to end of the ngrams list
    # Start from 1 because 0 is the initial state and has nothing before it
    for i in range(1, len(ngrams)):
        last_ngram = ngrams[i - 1]
        cur_ngram = ngrams[i]

        if last_ngram not in ngramCount:
            ngramCount[last_ngram] = {}
            sampleCount[last_ngram] = 0

        if cur_ngram not in ngramCount[last_ngram]:
            ngramCount[last_ngram][cur_ngram] = 0

        ngramCount[last_ngram][cur_ngram] += 1
        sampleCount[last_ngram] += 1

    return (ngramCount, sampleCount)
