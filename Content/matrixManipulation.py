# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# n = 35
# splited = []
# lenL = len(l)
# for i in range(n):
#     start = int(i*lenL/n)
#     end = int((i+1)*lenL/n)
#     splited.append(l[start:end])
# print(splited)

#contL == 0 or contL < n/contL | contL/n < 1

#      1,2,3,1,2,3,1,2,3
# lst = [1,2,3,4,5,6,7,8,9]
# def createProportion(n):
#     matrixF = []
#     line = []
#     cont = 0
#     contL = 0
#     while cont < len(lst):
#         if contL != n:
#             line.append(lst[cont])
#             contL += 1
#         else:
#             contL = 1
#             matrixF.append(line)
#             line = []
#             line.append(lst[cont])
#         cont += 1
#     matrixF.append(line)
#     return matrixF

# print(createProportion(3))#3x3

from this import d


lst = ["e","a","j","a","j","u","8","i","n","g","l","a","t","e","r","r","a","u","o","p","i","f","u","a","o","d","o","x","i","t","u","x","e","a"]
#new   -1  -1  -1  -1   0   1   2   3   4   5   6
x = str(lst)[1:-1].replace(", ","").replace("'","")
print(x)#normal
print(x[::-1])#reverse
print(x.find("inglaterra")+1)#f
# print(lst.index("a"))

# lst = ["s","a","l","d","o","c","e"]
x = str(lst)[1:-1].replace(", ","").replace("'","")
print(x)#normal
print(x[::-1])#reverse
print(x.find("saldoce"))#find=0 /notFound=-1

m= [["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t"],
    ["u", "v", "w", "x", "y"]]
    #a
    #fb
    #kgc
    #plhd
    #uqmie
    #vrnj
    #wso
    #xt
    #y
d = []

n = 5
lines = 0
indexLst=n-1#4
indexLetter=0
# while lines < n*2-1:#9
#     while indexLst < lines:
#         while indexLetter < :
#             m[indexLst][indexLetter]
#             indexLetter+=1
#         indexLst-=1
#     lines+=1
    
print("-----")
lst.append(m[0][0])
d.append(lst)
print("-----")
print(m[1][0])
print(m[0][1])
print("-----")
print(m[2][0])
print(m[1][1])
print(m[0][2])
print("-----")
print(m[3][0])
print(m[2][1])
print(m[1][2])
print(m[0][3])
print("-----")
print(m[4][0])
print(m[3][1])
print(m[2][2])
print(m[1][3])
print(m[0][4])
print("-----")
print(m[4][1])
print(m[3][2])
print(m[2][3])
print(m[1][4])
print("-----")
print(m[4][2])
print(m[3][3])
print(m[2][4])
print("-----")
print(m[4][3])
print(m[3][4])

print(m[4][4])

# columns in lines
# m = createProportion(n)#35x35
# lst = []
# contC = 0#column
# contl = 0
# c = 0
# while c < n*n:
#     if contl != n:
#         lst.append(m[contl][contC])
#         contl+=1
#     else:
#         contC+=1
#         contl = 0
#         print(lst)
#         lst=[]
#     c += 1