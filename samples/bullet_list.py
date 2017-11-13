import pyperclip

lists = pyperclip.paste()

lists = lists.strip().split('\n')
for i in range(len(lists)):
    lists[i] = '* ' + lists[i]

lists = '\n'.join(lists)

pyperclip.copy(lists)

print(lists)
