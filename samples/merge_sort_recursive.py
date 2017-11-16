def merge_sort(n):
    if len(n) < 2:
        return n[:]
    else:
        middle = len(n) // 2
        left = merge_sort(n[:middle])
        right = merge_sort(n[middle:])
        name = merge(left, rig)
        print(name)
        # return merge(left, right)


print(merge_sort([10, 2, 11, 4, 16, 3, 21, 12]))