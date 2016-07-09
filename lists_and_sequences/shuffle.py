import random


def shuffle(L):
    for i in range(len(L)-1, -1, -1):
        j = random.randint(0, i)
        L[i], L[j] = L[j], L[i]
