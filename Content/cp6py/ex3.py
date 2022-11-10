
#pilha
from collections import deque

arr = [4,2,3,8,9,5,1,6,7]
auxArr = arr

# declaracao de pilha
stack1 = deque([])
stack2 = deque([])
stackRep1 = 0
stackRep2 = 0

def orderByStack(arr):
    #definir metades arr
    if len(arr)%2 != 0:
        stackRep1 = len(arr)//2
        stackRep2 = len(arr)//2 + 1
    else:
        stackRep1 = len(arr)//2
        stackRep2 = len(arr)//2
    # pegar metade abaixo nums
    c = 0
    while c < stackRep1:
        getMin = min(auxArr)
        auxArr.remove(getMin)
        stack1.append(getMin)
        c+=1
    
    # pegar metade acima nums
    c = 0
    while c < stackRep2:
        getMin = min(auxArr)
        auxArr.remove(getMin)
        stack2.append(getMin)
        c+=1

orderByStack(arr)
order = stack1+stack2
print("\nORDENATION \n",order)