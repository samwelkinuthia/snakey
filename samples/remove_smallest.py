def rem(n):
    if n:
        n.remove(min(n))
    return n

n = [99, 10, 139, 33, 28, 236, 199, 284, 396]
print(rem(n))