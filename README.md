# python
<img src="./Content/img/pythonCut.PNG"/>
Language for data Science</br>
https://panda.ime.usp.br/pensepy/static/pensepy/05-Funcoes/funcoes.html</br>
https://www.ime.usp.br/~macmulti/</br>

#### Code
- intall Python
- add extention Python VScode
```python
run code
#C:\Users\logonrmlocal
#c:/python39/python ./nomeExemplo.py
#quit() sair do cmd
```
#### Logical Operators
| Operator | Character |
| --- | --- |
| add | + |
| subtraction | - |
| multiplication | * |
| real division | / |
| rest division | % |
| integer division | // |
| potency | ** |

#### Conditional Operators
| Operator | Character |
| --- | --- |
| igual | == |
| menor | < |
| maior | > |
| diferente | != |
| menor ou igual | <= |
| maior ou igual | >= |

#### Fibonacci sequence
f1 = 1</br>
f2 = 1</br>
f3 = f2 + f1</br>
f4 = f3 + f2</br>
...</br>

```python
# ask = input("Write 1 value:")
# num1 = int(valor)
# ask = input("Write 1 value:")
# num2 = int(valor)
#plus = num1 + num2
#print(plus)

num1 = input("Write 1 value:")
num2 = input("Write 2 value:")
num3 = input("Write 3 value:")
num4 = input("Write 4 value:")
print(int (num1) + int (num2) + int (num3) + int (num4))
```

```python
#armazena a resposta do usuario
test = input("seu texto? ")
#print variable
print(test)

#.txt .dat
print("Salvando arquivo...")
arquivo = open("questionario.dat", mode='w')
#write and jump line
arquivo.write(test + "\n")
#close for save
arquivo.close()

# dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
# dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
# wsl --set-default-version 2
```
#### Validations
- algotitimo modulo 11(cpf)
  ABC.DEF.GHI-JK
  
  ##### calc J
  - 10.A + 9.B + 8.C + 7.D + 6.E + 5.F + 4.G + 3.H + 2.I
  - rest % 11
  - (j = 0)rest < 2
  - (j = rest - 11)rest >= 2
  
  ##### calc K
  - 11.A + 10.B + 9.C + 8.D + 7.E + 6.F + 5.G + 4.H + 3.I + 2.J
  - rest % 11
  - (j = 0)rest < 2
  - (j = rest - 11)rest >= 2
  
  
- algoritimo modulo 10(boleto)
- tabela ascII
  letters in binary
 
 ##### NUMBERS
 -binary
  10560 = 1.10⁴ + 0.10³ + 5.10² + 6.10¹ + 0.10⁰
  
 - hexadecimal

 - decimal
 
 ##### FUNCTIONS
```python
def calc(a,b):
  result = a + b
  return result
finalValue = calc(5,2)
print(finalValue)
```
##### TUPLAS (jogo de baralho)
##### LIST (jogo de domino)
##### MATRIZES (processamento de imagens/ caca palavras)
##### ALGORITIMOS DE BUSCA E ORDENACAO
##### DICTIOARY
##### PILHA E FILA(sudoku, problema do labirinto)
##### RECURSAO(funcao que retorna outra funcao)
