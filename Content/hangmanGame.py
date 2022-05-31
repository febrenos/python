import random
words = ["Melancia", "Pera", "telescopio", "Retroprojetor", "pneumoultramicroscopicossilicovulcanoconiotico"]
lenWords = len(words)-1
random = random.randint(0, lenWords)
word = words[random]
# print("\n", word)

def putDash(word):
    aux = ""
    for c in word:
        aux = aux + "_ "
    return aux

def verifyGuess(word, secret, guess):
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
secret = putDash(word)

while erros < 6 and "_" in secret:
    print("\n", secret)
    print("Erros: ", erros)
    chute = input("Letra: ")
    secret = verifyGuess(word, secret, chute)
    if not chute in word:
        erros = erros + 1

if erros >= 6:
    print("\n", "Você perdeu, a palavra era ", word)
else:
    print("\n", secret)
    print("Parabéns, você acertou!")
