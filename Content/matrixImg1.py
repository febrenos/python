import Imagem
matriz = Imagem.getMatrizImagemCinza('olhos.jpg')

print("Linhas=", len(matriz))
print("Colunas=", len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 128:
            matriz[i][j] = 255
        else:
            matriz[i][j] = matriz[i][j] - 64
            if matriz[i][j] < 0:
                matriz[i][j] = 0

Imagem.salvaImagemCinza('olhos_modificado.jpg', matriz)
print('Finish')
