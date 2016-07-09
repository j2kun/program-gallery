from randomized.primality import probablyPrime
import random


def goodPrime(p):
    return p % 4 == 3 and probablyPrime(p, accuracy=100)


def findGoodPrime(numBits=512):
    candidate = 1

    while not goodPrime(candidate):
        candidate = random.getrandbits(numBits)

    return candidate


def makeModulus():
    return findGoodPrime() * findGoodPrime()


def parity(n):
    return sum(int(x) for x in bin(n)[2:]) % 2


class BlumBlumShub(object):
    def __init__(self, seed=None):
        self.modulus = makeModulus()
        self.state = seed if seed is not None else random.randint(2, self.modulus - 1)
        self.state = self.state % self.modulus

    def seed(self, seed):
        self.state = seed

    def bitstream(self):
        while True:
            yield parity(self.state)
            self.state = pow(self.state, 2, self.modulus)

    def bits(self, n=20):
        outputBits = ''

        for bit in self.bitstream():
            outputBits += str(bit)
            if len(outputBits) == n:
                break

        return outputBits


if __name__ == "__main__":
    generator = BlumBlumShub()

    hist = [0] * 2**6
    for i in range(10000):
        value = int(generator.bits(6), 2)
        hist[value] += 1

    print(hist)
