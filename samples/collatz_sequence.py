def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        result = (3 * num + 1)
        print(result)
        return(result)

number = input("Number?")
while number != 1:
    try:
        number = collatz(int(number))
    except ValueError:
        print("enter a valid integer")
