def calc(c):
    num = 0
    vogal = 0
    lenC = len(c)
    while lenC != 0:
        lenC = lenC - 1
        getI = c[lenC]
        if getI == "1" or getI == "2" or getI == "3" or getI == "4" or getI == "5" or getI == "6" or getI == "7" or getI == "8" or getI == "9":
            num = num + 1
        if getI == "A" or getI == "B" or getI == "C" or getI == "D" or getI == "E" or getI == "F" or getI == "G" or getI == "H" or getI == "I" or getI == "J" or getI == "K" or getI == "L" or getI == "M" or getI == "N" or getI == "O" or getI == "P" or getI == "Q" or getI == "R" or getI == "S" or getI == "T" or getI == "U" or getI == "V" or getI == "W" or getI == "X" or getI == "Y" or getI == "Z":
            vogal = vogal + 1
    if num != 8:
        print("Precisam haver exatamente 8 numeros")
    elif vogal != 7:
        print("Precisam haver exatamente 7 vogais maiusculas")
    elif len(c) != 15:
        print("Precisam haver 15 caracteres")
    else:
        print("OK")
print(calc("12345678eeeeeee"))