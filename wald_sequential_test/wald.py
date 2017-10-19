from math import log
import random


def biased_coin(p):
    while True:
        yield 1 if random.random() < p else -1


def wald_sequential_test(lower, upper, sequence, error_tolerance=0.01, max_rounds=1000):
    '''
        Distinguish between a coin with bias at most `lower` or at
        least `upper` with confidence at least 1 - error_tolerance

        lower, upper are floats in (0,1), and sequence is an iterable of +/-1
    '''

    # the possibilities are reversed: the first index denotes the value we track for
    # the upper bound, the second index tracks the lower bound
    possibilities = exceeds_upper, at_most_lower = [0, 0]
    labels = ["p >= %.2f" % upper, "p <= %.2f" % lower]

    threshold = log(1 - error_tolerance) - log(error_tolerance)
    # print("Threshold is %.2f" % threshold)
    log_likelihood = (
        log(lower * (1 - upper)) -
        log(upper * (1 - lower))
    )

    for i, coin in enumerate(sequence):
        # print(possibilities)
        if i > max_rounds:
            return "Indeterminate"

        for s in [-1, 1]:
            index = int((s + 1) / 2)
            possibilities[index] += s * coin * log_likelihood
            if possibilities[index] > threshold:
                return labels[index]


if __name__ == "__main__":
    from collections import Counter
    trials = [wald_sequential_test(0.5, 0.6, biased_coin(0.49)) for _ in range(10000)]
    print(Counter(trials))
