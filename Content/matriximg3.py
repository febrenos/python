import Imagem

matriz = Imagem.getMatrizImagemColorida('lago_canada.jpg')

matrizR = matriz[0]
matrizG = matriz[1]
matrizB = matriz[2]

for i in range(len(matrizB) // 3):
    for j in range(len(matrizB[0]) // 3):
        matrizR[i][j] = matrizR[i][j] + 50
        matrizG[i][j] = matrizG[i][j] + 50
        matrizB[i][j] = matrizB[i][j] + 50

Imagem.salvaImagemColorida('new_lago_canada.jpg', matrizR, matrizG, matrizB)
#Imagem.salvaImagemColorida('new_lago_canada.jpg', matrizR, matrizG, matrizB)
print("OK")
