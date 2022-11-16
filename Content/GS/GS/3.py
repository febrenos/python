def calc(c):
    quantity = 0
    lenC = len(c)
    while lenC != 0:
        lenC = lenC - 1
        getI = c[lenC]
        if getI == "1" or getI == "2" or getI == "3" or getI == "4" or getI == "5" or getI == "6" or getI == "7" or getI == "8" or getI == "9":
            quantity = quantity + 1
    return quantity
print(calc("1223eeeeeeeeee"))