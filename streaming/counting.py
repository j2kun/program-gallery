import random
import statistics


def randomHash(modulus):
    a, b = random.randint(0, modulus-1), random.randint(0, modulus-1)

    def f(x):
        return (a*x + b) % modulus

    return f


def numDistinctElements(stream, numParallelHashes=10):
    modulus = 2**20
    hashes = [randomHash(modulus) for _ in range(numParallelHashes)]
    minima = [modulus] * numParallelHashes
    currentEstimate = 0

    for i in stream:
        hashValues = [h(i) for h in hashes]
        for i, newValue in enumerate(hashValues):
            if newValue < minima[i]:
                minima[i] = newValue

        currentEstimate = modulus / statistics.mean(minima)

        yield currentEstimate


if __name__ == "__main__":
    S = range(10000)   # [random.randint(1,2**20) for _ in range(10000)]

    for k in range(10, 301, 10):
        for est in numDistinctElements(S, k):
            pass
        print(abs(est))
