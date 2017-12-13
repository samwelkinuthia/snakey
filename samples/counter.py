import pprint


def counter(words):
    count = {}
    for i in words:
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    return count


words = input("Enter the sentence you want to be counted: ")

pprint.pprint(counter(words))

