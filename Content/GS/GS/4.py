def calc(c):
    num = 0
    vogal = 0
    lenC = len(c)
    while lenC != 0:
        lenC = lenC - 1
        getI = c[lenC]
        if getI == "1" or getI == "2" or getI == "3" or getI == "4" or getI == "5" or getI == "6" or getI == "7" or getI == "8" or getI == "9":
            num = num + 1
        if getI == "a" or getI == "b" or getI == "c" or getI == "d" or getI == "e" or getI == "f" or getI == "g" or getI == "h" or getI == "i" or getI == "j" or getI == "k" or getI == "l" or getI == "m" or getI == "n" or getI == "o" or getI == "p" or getI == "q" or getI == "r" or getI == "s" or getI == "t" or getI == "u" or getI == "v" or getI == "w" or getI == "x" or getI == "y" or getI == "z":
            vogal = vogal + 1
    if num != 8:
        print("Precisam haver exatamente 8 numeros")
    elif vogal != 7:
        print("Precisam haver exatamente 7 vogais minusculas")
    elif len(c) != 15:
        print("Precisam haver 15 caracteres")
    else:
        print("OK")
print(calc("12345678eeeeeee"))