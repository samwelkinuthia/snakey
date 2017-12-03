def find(n):

# check for the common difference
# new array using the common difference
# check for difference between the two
# return the difference

    dif = n[1] - n[0]
    diff = n[2] - n[1]
    minm = min(diff, dif)
    new=[n[1] -minm]

    for i in range(len(n) - 1):
        new.append(n[i] + minm)
    x = list(set(new) - set(n))
    return x[0]

n =[2,4,6,8,12,14,16,18,20,22,24,26,28]
print(find(n))



