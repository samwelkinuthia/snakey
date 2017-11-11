students = {'sam':{'maths': 100, 'english': 50},
            'alice':{'maths': 100, 'english': 80},
            'tim':{'maths':200, 'english':40}}

def total(s, item):
    t = 0
    for k, v in s.items():
        t = t + v.get(item, 0)
        all = int(len(k))
        avg = t // all
    return avg

print("Average grade for maths: " + str(total(students, 'maths')))