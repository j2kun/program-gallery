from math import log
import random


def biased_coin(p):
    while True:
        yield 1 if random.random() < p else -1


def wald_sequential_test(lower, upper, sequence, error_tolerance=0.01):
    '''
        Distinguish between a coin with bias at most `lower` or at
        least `upper` with confidence at least 1 - error_tolerance

        lower, upper are floats, and sequence is an iterable of +/-1
    '''

    possibilities = at_most_lower, exceeds_upper = [0, 0]
    threshold = log(1 - error_tolerance) - log(error_tolerance)
    log_likelihood = (
        log(lower) + log(1 - upper) -
        log(upper) - log(1 - lower)
    )

    for coin in sequence:
        for s in [-1, 1]:
            index = int(s + 1) / 2
            possibilities[index] += s * coin * log_likelihood
            if possibilities[index] > threshold:
                return index
