# recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
print(fatorial(6))

# interativa
def fat(n):#fatorial interativa por causa do while
    value = 1
    while n > 0:
        value= value *n
        n = n - 1
    return value
print(fat(6))
