import re

def reverse(x):
    y = re.split(r'(\s+)', x)
    print(y)
    new = []
    for i in y:
        i = i[::-1]
        new.append(i)
    return ''.join(new)


x = "samwel what are you doing??"
print(reverse(x))
