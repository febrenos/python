#2
#precisa mostrar a pos da repeticao usando busca binaria
arr = [0, 10, 20, 30, 50, 50, 60, 60, 70, 70, 70, 70, 70]
auxArr = arr
lst = []
n = [0]

repeat = 0
for i in auxArr:
    if i == 70:
        repeat+=1 #3

# busca binaria
def binaryRecursive(vector, init, last, item):
    n[0] = item
    if last < init:
        return -1
    med = init
    if vector[med] == item:
        lst.append(med)
        auxArr[med] = 0
        init = 0
        last = len(auxArr)
        return med
    elif vector[med] > item:
        return binaryRecursive(vector, init, med - 1, item)
    else:
        return binaryRecursive(vector, med + 1, last, item)
c=0
while c < repeat:
    binaryRecursive(auxArr, 0, len(auxArr) - 1, 60)
    c+=1

print(f"\nNUM:{n} \nposition(s):{lst}")