
def majority(stream):
    stream = iter(stream)
    held = next(stream)
    counter = 1

    for item in stream:
        if item == held:
            counter += 1
        elif counter == 0:
            held = item
            counter = 1
        else:
            counter -= 1

    return held


if __name__ == "__main__":
    print(majority("abbbaabbabababbba"))
    print(majority("a"*100 + "b"*99 + "cc"))
