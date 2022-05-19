#get numbers of repetitions
lst = [1,2,3,3,1,99,99,99,99,1]
repeateds = []
repeated = []
valores = []

for i in lst:
    if lst.count(i) != 1:
        repeateds.append(i)
    if lst.count(i) != 1 and i not in repeated:
        repeated.append(i)
        
print("\nNUM REPEATEDS")    
lenRepeateds = len(repeateds)
lenRepeated = len(repeated)
result = lenRepeateds - lenRepeated
print(result)

#get numbers of repetitions
print("\nNUM REPEATEDS")
lst = []
lstRepeteds = []
values = []
repetitionsLoop = 0
nsequence = int(input("how much sequence: "))
listCount = len(lst)#8
nsequenceMore = 0

#add num in lst
while repetitionsLoop < nsequence:
    print(lst)
    print("\nmore:", nsequence - repetitionsLoop, "number(s)")
    repetitionsLoop = repetitionsLoop + 1
    n = int(input("Number: "))
    lst.append(n)

repetitionsLoop = 0
#add all repeteds in list(lstRepeteds)
while repetitionsLoop < nsequence:
    repetitionsLoop = repetitionsLoop + 1
    listCount = listCount - 1
    getNum = lst[listCount]
    repeat = lst.count(getNum)
    if repeat != 1 and getNum not in lstRepeteds:
        lstRepeteds.append(getNum)

# get hom many the repetion
lenRepeteds = len(lstRepeteds)
getNum = 0
for i in lstRepeteds:
    lenRepeteds = lenRepeteds - 1
    getNum = lstRepeteds[lenRepeteds]
    count = lst.count(getNum)
    values.append(count)

print("\n", lst)
print("Number(s) duplication:",lstRepeteds)
values = sum(values) - len(values)
print("Repeated:", values)
