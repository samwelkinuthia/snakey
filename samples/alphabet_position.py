import re
import string

def alph(text):
    a = list(string.ascii_lowercase)
    reg = re.compile(r'[^a-z]')
    di = {}
    for i in range(len(a)):
        di[i + 1] = a[i]
    text = text.lower()
    text = reg.sub('', text)
    text=list(text)
    for i in range(len(text)):
        for k,v in di.items():
            if text[i] in v:
                text[i] = str(k)
    return str(' '.join(text))

print(alph('The sunset sets at twelve o\' clock.'))