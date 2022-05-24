def coloca_traco(word):
    aux = ""
    for c in word:
        aux = aux + "_ "
    return aux

def verifica_chute(word, secret, guess):
    aux = ""
    i = 0
    while i < len(word):
        if word[i] == guess:
            aux = aux + guess + " "
        else:
            aux = aux + secret[2 * i] + " "
        i = i + 1
    return aux    


erros = 0
palavra = "Melancia"
segredo = coloca_traco(palavra)

while erros < 6 and "_" in segredo:
    print(segredo)
    print("Erros: ", erros)
    chute = input("Letra: ")
    segredo = verifica_chute(palavra, segredo, chute)
    if not chute in palavra:
        erros = erros + 1

if erros >= 6:
    print("Você perdeu, a palavra era ", palavra)
else:
    print(segredo)
    print("Parabéns, você acertou!")    
