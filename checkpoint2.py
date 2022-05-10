#1
print("\nNUM REPEATEDS")
lst = []
initLst = []
numBefore = 0
n = int(input("How many Numbers: "))
repeatLoop = 0
while repeatLoop < n:
    repeatLoop = repeatLoop + 1
    num = int(input("Number: "))
    initLst.append(num)
    if num != numBefore:
        lst.append(num)
    numBefore = num
    
print(initLst)
print(len(lst))

#2
print("\nPRODUCTS VALUE")
n = int(input("Quantity of products: "))
lstDifValue = []
lstPercent = []
repeatLoop = 0
while repeatLoop < n:
    repeatLoop = repeatLoop + 1
    print("Product")
    oldValue = float(input("Old value: "))
    actualValue = float(input("New value: "))
    difValue =  actualValue - oldValue
    percent = ((actualValue - oldValue)/oldValue)*100
    lstDifValue.append(difValue)
    lstPercent.append(percent)

print("Difference value: ", lstDifValue)
print("Percentual: ", lstPercent)
lstDifValue = max(lstDifValue)
print("Higher value: ", "R$", "{: .2f}".format(lstDifValue))
lstPercent = max(lstPercent)
print("Higher percentual: ", "{: .2f}".format(lstPercent),"%")

#3
print("\nMONEY EXCHANGE")
money = int(input("Total money: "))
coin1 = int(input("First coin value: "))
coin2 = int(input("Second coin value: "))
coinMore = 0 #soma alternada
coin1Count = 0
coin2Count = 0

# priorizar o maior valor
if money % coin1 == 0 and coin1 > coin2:
    print(f"\nFirst coin: {money//coin1} x {coin1}coin(s)")
    coinMore = coinMore + money
if money % coin2 == 0 and coin1 < coin2:
    print(f"\nSecond coin: {money//coin2} x {coin2}coin(s)")
    coinMore = coinMore + money
if money % coin2 != 0 and money % coin1 == 0 and coin1 < coin2:
    print(f"\nFirst coin: {money//coin1} x {coin1}coin(s)")
    coinMore = coinMore + money
if money % coin1 != 0 and money % coin2 == 0 and coin1 > coin2:
    print(f"\nFirst coin: {money//coin2} x {coin2}coin(s)")
    coinMore = coinMore + money

# coin1=impar coin2=impar
if  coin1 % 2 != 0 and coin2 % 2 != 0 and (money - coin2)%coin1 == 0:
    coin1Count = (money - coin2)//coin1
    coin2Count = coin2Count + 1
    
if  coin1 % 2 != 0 and coin2 % 2 != 0 and (money - coin1)%coin2 == 0:
    coin2Count = (money - coin2)//coin2
    coin1Count = coin1Count + 1

# pegar unidade de cada coin
unityCoin1 = (coin1*2)%10
unityCoin2 = (coin2*2)%10
while coinMore != money and (money - coin2)%coin1 != 0 and (money - coin1)%coin2 != 0:
    if unityCoin1 % coin2 == 0 and (money - coin1*2)%coin2 == 0 and money > coin1*2:
        coin1Count = coin1Count + 2
        coin2Count = coin2Count + (money - coin1*2)//coin2
        coinMore = coinMore + coin1*2 + money - coin1*2

    if unityCoin2 % coin1 == 0 and (money - coin2*2)%coin1 == 0 and money > coin2*2:
        coin2Count = coin2Count + 2
        coin1Count = coin1Count + (money - coin2*2)//coin1
        coinMore = coinMore + coin2*2 + money - coin2*2

    if unityCoin1 % coin2 != 0 and unityCoin2 % coin1 != 0 or coin1Count*coin1 + coin2Count*coin2 != money:
        print("IS NOT POSSIBLE TO COVERT")
        print(coinMore)
        break

if coin1Count*coin1 + coin2Count*coin2 == money:
    print(f"Second coin: {coin1Count} x {coin1}coin(s)")
    print(f"Second coin: {coin2Count} x {coin2}coin(s)")
