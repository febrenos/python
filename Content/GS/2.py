def calc():
    avaliacao = -1
    melhorAvaliado = []
    while avaliacao != 0:
        produto = input("\nNome do produto: ")
        avaliacao = int(input("Avaliacao do produto: "))

        melhorAvaliado.append(produto)
    return melhorAvaliado
print(calc())