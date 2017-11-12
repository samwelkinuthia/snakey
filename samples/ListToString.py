def stringify(item):
    for i in item:
        print(i + ',', end='')
        if i == item[-1]:
            print('and ' + item[1],  end='')
            break

item = ['apples', 'bananas', 'tofu', 'cats']


stringify(item)
