def pic(i, left, right):
    print('items'.center(left+right, '*'))
    for k,v in i.items():
        print(k.ljust(left, '.') + str(v).rjust(right))


i = {'name': 4, 'tea':40, 'wine':70}
pic(i, 20, 14)