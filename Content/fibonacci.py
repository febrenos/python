# ver se esta perto da razao aurea
# 1 1 2 3 5 8 13 21
# 1/1=1
# 1/2 = 1.5

#recursive
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

#interative
def fib(n):
    ant1 = 1
    ant2 = 1
    while n > 2:
        actual = ant1 + ant2
        ant1 = ant2
        ant2 = actual
        n = n - 1
    return actual
print(fib(6))

def fibTcr(n,a,b):
    if n == 0: 
        return a
    if n == 1: 
        return b
    return fibTcr(n-1,b,a+b)
