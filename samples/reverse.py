def reverse(x):
    y = x.split()
    new = []
    for i in y:
        i = i[::-1]
        new.append(i)
    return ' '.join(new)


x = "double  spaces"
print(reverse(x))
