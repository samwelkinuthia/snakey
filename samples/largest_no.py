def max(n):
    largest = 0
    for i in n:
        if i > largest:
            largest = i
    return largest

print(max([11, 2, 14, 5, 0, 19, 21]))