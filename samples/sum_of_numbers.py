def sum_of_num(num):
    sum = 0
    while(num):
        sum += num % 10
        num = num // 10
    return sum

print("Max value is: ", max(234, 578, 2309, 999, key=sum_of_num))

