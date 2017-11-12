students = []
while True:
    print('Enter student ' + str(len(students) + 1) + '(Or you can stop if full): ')
    name = input()
    if name == '':
        break
    students = students + [name]
print('the names are:')
for name in students:
    print(name)
