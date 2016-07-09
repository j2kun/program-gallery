def streamingMedian(seq):
    seq = iter(seq)
    m = 0

    for nextElt in seq:
        if m > nextElt:
            m -= 1
        elif m < nextElt:
            m += 1

        yield m
