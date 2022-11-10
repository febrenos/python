dicionario = [{'chave1': [50,30], 'chave2': [10,27], 'chave3':[7,55], 'chave4': [41,3]}]
def function():
    l_chaves = []
    l_values = []

    for lista in dicionario:
        for j, v in lista.items():
            l_chaves.append(j)
            l_values.append(v)

    #print(l_chaves)
    #print(l_values)
    return f"\nchaves: {l_chaves} \nvalores: {l_values}"
print(function())