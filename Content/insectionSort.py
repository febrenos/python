def organize(lst, pos):
    aux = lst[pos]

    while pos > 0 and lst[pos-1] > aux:
        lst[pos] = lst[pos-1]
        pos = pos - 1

    lst[pos] = aux

def selectionSort(lst):
    for i in range(1,len(lst)):
        organize(lst,i)

l = [2,3,5,0,3,6,9]
selectionSort(l)
print(l)
