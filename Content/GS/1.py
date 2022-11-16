# meses
m = int(input("Digite a quantidade de meses? "))
count = 0
finalValue = 0
while m > count:
    count = count + 1
    # valores
    v = float(input("Digite o valor faturado no mes? "))
    finalValue = finalValue + v
    
def calc(finalValue, m):
    finalValue = finalValue / m
    return finalValue

print(calc(finalValue, m))
