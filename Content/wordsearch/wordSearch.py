
n=35#proportion
#a:Append / w:overWrite / x:Create
arq = open("cacapalavra.txt", "r")# or mode="r / 'r') as arq:
lines = arq.readlines()#35
content = arq.read()

def isnum(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

first = False
second = False
matrix = []
words = []
for line in lines:
    v = line.replace("\n","")
    #words
    if first and second:
        words.append(v)
    #second num
    if isnum(v) and first:
        secondNum = v
        second = True
    #first num
    if isnum(v) and not first:
        firstNum = v
        first = True
    #matrix
    if not isnum(v) and not second:
        matrix.append(v)
arq.close()

def matrixToLst():
    generateMatrix = []
    for line in matrix:
        for letter in line:
            generateMatrix += letter
    return generateMatrix

unifyedMtx = matrixToLst()

def createProportion(n):#n x n
    matrixF = []
    line = []
    cont = 0
    contL = 0
    while cont < len(unifyedMtx):
        if contL != n:
            line.append(unifyedMtx[cont])
            contL += 1
        else:
            contL = 1
            matrixF.append(line)
            line = []
            line.append(unifyedMtx[cont])
        cont += 1
    matrixF.append(line)
    return matrixF

# WORDLIST
wl = open("wordList.txt", "w")
for l in words:
    wl.write(l)
    wl.write("\n")
wl.close()

# PRINT MATRIX
pws = open("printWordSearch.txt", "w")
lst = []
for line in createProportion(n):
    for letter in line:
        pws.write(f"{letter} ")
    pws.write("\n")
lst = []
pws.close()

# columns in lines
m = createProportion(n)#35x35
invertMatrix = []
lst = []
contC = 0#column
contl = 0
c = 0
while c < n*n:
    if contl != n:
        lst.append(m[contl][contC])
        contl+=1
    else:
        contC+=1
        contl = 0
        invertMatrix.append(lst)
        lst=[]
    c += 1

#diagonal /
diagonalLeft = []

#diagonal \
# COORDENATIONS
for findWord in words:
    #HORIZONTAL
    #east/west and leste/oeste
    c=0
    for line in matrix:
        lineInStr = str(line)[1:-1].replace(", ","").replace("'","")
        c+=1
        #pq +2?
        if lineInStr.find(findWord) != -1:
            print(f"{findWord}: line: {c} in column: {lineInStr.find(findWord)+2} in east(Leste) direction(normal)")
        if lineInStr.find(findWord[::-1]) != -1:
            print(f"{findWord}: line: {c} in column: {lineInStr.find(findWord[::-1])+1+len(findWord)} in West(Oeste) direction(reverse)")

    #VERTICAL
    #north/south norte/sul
    c=0
    for line in invertMatrix:
        lineInStr = str(line[::-1])[1:-1].replace(", ","").replace("'","")
        c+=1
        #chile 22/33
        if lineInStr.find(findWord[::-1]) != -1:
            print(f"{findWord}: line: {c-len(findWord)} in column: {n-(lineInStr.find(findWord[::-1])-1)} in South(Sul) direction(normal)")
        if lineInStr.find(findWord) != -1:
            print(f"{findWord}: line: {n-(lineInStr.find(findWord)-2)} in column: {c} in North(Norte) direction(reverse)")




#nordeste
#noroeste
#sudeste
#sudoeste
#https://www.w3schools.com/python/python_file_write.asp