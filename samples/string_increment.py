def inc(n):
    letters='abcdefghijklmnopqrstuvwxyz'
    x = []
    if n[len(n)-1] in letters:
        return n + str(1)
    else:
        for i in range(len(n)):
            if n[i] not in letters and n[i] != '0':
                x.append(n[i])
        for y in x:
            if y in n:
                n = n.replace(y, '')
                print(n)
        x = ''.join(x)
        x = int(x) + 1
        return n + str(x)
print(inc("foo0042 "))