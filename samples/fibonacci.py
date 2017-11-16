from functools import lru_cache
#store previous fibo results in cache

@lru_cache(maxsize = 1000)

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter nth value: "))

print("The " + str(n) + "th term is",  fibo(n))