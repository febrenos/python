import random

def cria_baralho():
    bar = []
    for naipe in ('♣', '♥', '♠', '♦'):
        valor = 1
        while valor <= 13:
            c = (valor, naipe)
            bar.append(c)
            valor = valor + 1

    return bar

def compra(bar):
    return bar.pop()


def distribui(bar, qtd):
    mao = []
    while qtd > 0:
        c = compra(bar)
        mao.append(c)
        qtd = qtd - 1

    return mao    

def imprime(mao):
    saida = ""
    for c in mao:
        if c[0] == 1:
            saida = saida + "A"
        elif c[0] == 11:
            saida = saida + "J"
        elif c[0] == 12:
            saida = saida + "Q"
        elif c[0] == 13:
            saida = saida + "K"
        else:
            saida = saida + str(c[0])
        saida = saida + c[1] + " "
    return saida

def embaralha(bar):
    for qtd in range(200):
        i = random.randint(0, len(bar) - 1)
        j = random.randint(0, len(bar) - 1)
        aux = bar[i]
        bar[i] = bar[j]
        bar[j] = aux
    
def soma_pontos(mao):
    soma = 0
    for carta in mao:
        if carta[0] > 10:
            soma = soma + 10
        else:
            soma = soma + carta[0]
    return soma                            

deck = cria_baralho()
embaralha(deck)
mao_jog = distribui(deck, 2)
mao_cpu = distribui(deck, 2)

saida = imprime(mao_jog)
print(saida)
resp = input("Quer carta? (s/n)")
while resp == 's':
    c = compra(deck)
    mao_jog.append(c)
    saida = imprime(mao_jog)
    print(saida)
    resp = input("Quer carta? (s/n)")

while soma_pontos(mao_cpu) < 16:
    c = compra(deck)
    mao_cpu.append(c)

print(imprime(mao_jog))
print("Pontos Jog: ", soma_pontos(mao_jog))
print(imprime(mao_cpu))
print("Pontos Cpu: ", soma_pontos(mao_cpu))