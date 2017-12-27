# fetch the string
# Check whether it ends with a number
# If so, add 1 to the number
# If not, add 1 to the string
# If the number is 0, dont do anything with it

def inc(n):
    x = []
    p = []
    for i in n:
        if i.isdigit():
            x.append(i)
            n = n.replace(i, '')
    for y in x:
        if y is '0':
            n = n + str(y)
        else:
            p.append(y)
    p = ''.join(p)
    p = int(p) + 1
    return n + str(p)


print(inc("foo0042"))