import random


def reservoirSample(stream):
    for k, x in enumerate(stream, start=1):
        if random.random() < 1.0 / k:
            chosen = x

    return chosen
