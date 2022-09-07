def  menor(lst, i):
    pos_menor = i 
    i = i + 1
    while i < len(lst):
        if lst[pos_menor] > lst[i]:
            pos_menor = i
        i = i + 1
    return pos_menor

conj = [2,-7,9,3,,10,15,6]

for i in range(len(conj))
j = menor(conj, i)
aux = conj[j]
conj[j] = conj[i]
conj[i] = aux

print(conj)
