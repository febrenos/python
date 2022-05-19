nome = input("Digite seu nome: ")
'''Felipe Breno Sugisawa Altran'''
idade = input("Digite sua idade: ")
'''19'''
curso = input("Ja fez algum curso superior? ")
'''ADS(senai), RocketSeat'''
ti = input("Por que escolheu Tecnologia da Informacao (TI)? ")
'''Amo a tecnologia e as possibilidades de mudar o mundo'''
workTi = input("Dentro de TI, ja sabe no que voce gostaria de trabalhar? ")
'''Busco trabalho como desenvolvedor FullSatck, ja trabalhei na area e nao e tao facil quanto parece'''
hobbies = input("Quais sao seus hobbies? ")
'''Pratico esportes, toco guitarra e violao'''

'''print all'''
print(nome)
print(idade)
print(curso)
print(ti)
print(workTi)
print(hobbies)

'''.txt .dat'''
print("Salvando arquivo...")
arquivo = open("questionario.dat", mode='w')
arquivo.write(nome + "\n")
arquivo.write(idade + "\n")
arquivo.write(curso + "\n")
arquivo.write(ti + "\n")
arquivo.write(workTi + "\n")
arquivo.write(hobbies + "\n")
arquivo.close()

'''C:\Users\logonrmlocal'''
'''quit() sair do cmd'''
'''c:/python39/python ./questionario.py'''