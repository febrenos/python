import fila

def criaLabirinto(dimLin, dimCol):
    matriz = []
    for i in range(dimLin):
        matriz.append([-1] * dimCol)

    matriz[0][2] = matriz[0][3] = -9
    matriz[1][1] = matriz[1][4] = matriz[1][6] = matriz[1][8] = matriz[1][9] = -9       
    matriz[2][2] = matriz[2][4] = matriz[2][6] = matriz[2][10] = -9         
    matriz[3][1] = matriz[3][3] = matriz[3][7] = matriz[3][8] = -9        
    matriz[4][3] = matriz[4][5] = matriz[4][9] = -9
    matriz[5][1] = matriz[5][8] = -9

    return matriz


mat = criaLabirinto(6, 11)
lista = []
    
fila.put(lista, (0, 0))
mat[0][0] = 10
lin = 0
col = 0

while not fila.isEmpty(lista) and (5, 10) != (lin, col):
    pos = fila.get(lista)
    lin = pos[0]
    col = pos[1]

    #verificar os vizinhos em branco
    #norte
    if lin - 1 >= 0 and mat[lin-1][col] == -1:
        mat[lin-1][col] = mat[lin][col] + 1
        fila.put(lista, (lin-1, col))

    #sul
    if lin + 1 <= 5 and mat[lin+1][col] == -1:
        mat[lin+1][col] = mat[lin][col] + 1
        fila.put(lista, (lin+1, col))

    #leste
    if col + 1 <= 10 and mat[lin][col+1] == -1:
        mat[lin][col+1] = mat[lin][col] + 1
        fila.put(lista, (lin, col+1))

    #oeste
    if col - 1 >= 0 and mat[lin][col-1] == -1:
        mat[lin][col-1] = mat[lin][col] + 1
        fila.put(lista, (lin, col-1))

for lin in mat:
    print(lin)