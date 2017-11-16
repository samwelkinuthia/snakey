def bubble_sort(n):
    swap = False
    while not swap:
        print('bubble sort: ' + str(n))
        swap = True
        for j in range(1, len(n)):
            if n[j - 1] > n[j]:
                swap = False
                temp = n[j]
                n[j] = n[j - 1]
                n[j-1] = temp

test = [2, 4, 16, 49, 498, 5487, 12, 45, 6, 45, 6, 8, 9, 9, 8, 9]

print('')
print(bubble_sort(test))
print(test)
