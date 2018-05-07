def selection_sort(n):
    first=0
    while first != len(n):
        for i in range(first, len(n)):
            if n[i] < n[first]:
                n[first], n[i] = n[i], n[first]
            print(n)
        first += 1
    return n


print(selection_sort([1, 10, 5, 20, 56, 2193, 19328, 435, 12, 45, 76, 14, 45]))