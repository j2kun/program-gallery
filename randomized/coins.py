from random import random
from itertools import repeat


def fairCoin(biasedCoin):
    coin1, coin2 = 0, 0
    while coin1 == coin2:
        coin1, coin2 = biasedCoin(), biasedCoin()
    return coin1


# assume 0 < p < 1
def binaryDigits(decimal):
    while True:
        decimal *= 2
        yield int(decimal)
        decimal = decimal % 1


def biasedCoin(binaryDigitStream, fairCoin):
    fairBitStream = (fairCoin() for _ in repeat(1))
    for i, j in zip(binaryDigitStream, fairBitStream):
        if i != j:
            return i


if __name__ == "__main__":
    # examples
    def exampleBiasedCoin():
        return int(random() < 0.2)

    def exampleFairCoin():
        return int(random() < 0.5)

    import math
    p = math.pi % 1
    L = sum(biasedCoin(binaryDigits(p), fairCoin)
            for _ in range(100000)) / 100000.
