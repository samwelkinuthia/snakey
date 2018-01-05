def get_length_of_missing_array(arr):
    if not arr:
        return 0

    lengths = []
    for a in arr:
        if type(a) != list or len(a) == 0:
            return 0
        lengths += [len(a)]

    for i in range(min(lengths), max(lengths) + 1):
        if i not in lengths:
            return i