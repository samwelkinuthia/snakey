students = []
while True:
    print('Enter student ' + str(len(students) + 1) + '(leave blank to stop): ')
    name = input()
    if name == '':
        break
    students = students + [name]
print('the names are:')
for name in students:
    print(name)
