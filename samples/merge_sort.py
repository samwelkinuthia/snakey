def merge(left, right):
    # empty dic to hold data.
    result = []
    # i and j, two indices, beginning of both right and left list
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result

print(merge([3,11,4,6,10]))