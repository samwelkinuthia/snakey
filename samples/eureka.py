import math
def eureka(x, y):
    out=[]
    for i in range(x,y+1):
        i = str(i)
        if len(i) == 1:
            out.append(int(i))
        if len(i) > 1:
            total = 0
            if len(i) == 2:
                total = int(math.pow(int(i[0]), 1) + math.pow(int(i[1]), 2))
            elif len(i) == 3:
                total = int(math.pow(int(i[0]), 1) + math.pow(int(i[1]), 2) + math.pow(int(i[2]), 3))
            elif len(i) == 4:
                total = int(math.pow(int(i[0]), 1) + math.pow(int(i[1]), 2) + math.pow(int(i[2]), 3) + math.pow(int(i[3]), 4))
            if str(total) == i:
                out.append(int(total))
    return out
print(eureka(1, 2000))
