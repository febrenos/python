#INIT 1
import pandas as pd
df = pd.read_csv('test.csv')
df.head()#first 5
df.info()#verify data(null, empty, kind of values...)
df['data'] = pd.to_datetime(df['data'])# covert value to DateTime
import matplotlib.pyplot as plt # %matplotlib inline (view graphics)
plt.figure(figsize=(15,8))
plt.plot(df['data'], df['temperatura'])# view graphics eixo(y, x)
plt.title('Temperatura no tempo')# title in graphic

# use eixo for manipulation
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])# create eixo
eixo.plot(df['data'], df['temperatura'], color='green')#(y,x, color)
eixo.set_title('Temp', fontsize=25)#title in eixo graphic
eixo.set_ylabel('Temp', fontsize=20)# title y values
eixo.set_xlabel('Data', fontsize=20)# title x values
eixo.legend(['tempertura'], loc='lower right', fontsize=15)#(local of legend, localization, fontsize)

#INIT 2
# TItulo 01(colaby)
# !pip install 
import numpy as np
arr = np.arange(6)
arr
arr.reshape(2,3)
type(arr)
for i in range(6):
    print(i)

import pandas as pd
# storage
dados = pd.read_csv('test.csv')

# DATAFRAME COTINUO
# # Recebendo os dados:
from google_drive_downloader import GoogleDriveDownloader as gdd


data_google_id = '1ys03MPOO5Yn2XE8aBai3HkCkVE16EhtC'
gdd.download_file_from_google_drive(file_id=data_google_id, 
                                    dest_path = './dados.csv', # Faz o download dos dados e salva o mesmo num arquivo nomeado data.csv
                                    showsize = True)

# Armazenandos os dados em um DataFrame
dados = pd.read_csv("dados.csv", sep = ';')

type(dados) #type storage
dados.head()#first 5
dados.tail()#last 5
dados.info()#data type values
dados.shape #(lines/columns)

#FILTRANDO DADOS
dados.column
type(dados.column)
dados[["column","column","column"]]
dados[["column","column","column"]].head()
dados.iloc[[1,4], [1,5]]#view i by line/colunms
dados.iloc[0:10, [1,5]]#quantity items
dados.loc[:,["X1","X5"]]#all data
dados.loc[10:20,"X1":"X4"]#data interval, columns X1 at X4
dados.column >= 50# create mask
dados.X1 == "Male"# create mask
(dados.X1 == "Male") & (dados.X2 >=50)#|
dados[(dados.X1 == "Male") | (dados.X2 >=50)]#return only in true lines
dados[["X1","X2"]][(dados.X1 == "Male") & (dados.X2 >=50)]#especify columns to filt

#ACESS STATIC VALUES
media_X2 = dados.X2.mean()
mediana_X2 = dados.X2.median()
min_X2 = dados.X2.min()
max_X2 = dados.X2.max()
desvpad_X2 = dados.X2.std()
#25% 50% 75% sao quartils(grupos em % com relacao a popu.) (50% = mediana)
dados.describe()

print(f"Média: {media_X2} \nMediana: {mediana_X2}\nMinimo: {min_X2} \nMáximo: {max_X2}\nDesvio padrão: {desvpad_X2}" )

#FUNCTIONS FOM NEW COLUMNS
dados["X11"] = dados.X2**2
dados.head()

def normalizacao(valor):
  return (valor - min_X2)/(max_X2-min_X2)
dados["X12"] = dados.X2.apply(normalizacao)
dados["X12"]

#REMOVE COLUMNS
dados.drop(columns=["X11","X12"])#just for see
dados.drop(columns=["X11","X12"],inplace=True)#save data

#EXPLORATORY ANALYSIS
dados.columns = ["Id","Genero","Idade","Hipertensão","DoencaCoracao","JaFoiCasado","Sintomas","NivelGlucose",
                    "IMC","Fumante","AVC"]
dados.info()

# CATEGORIC DATA
import seaborn as sbn
import matplotlib.pyplot as plt

#  plot graphic with variáveis categóricas
colunas_categoricas = ["Genero", "Hipertensão", "DoencaCoracao", "JaFoiCasado", "Sintomas", "Fumante", "AVC"]
plt.figure(figsize=(40,40))
plt.subplots_adjust(hspace=0.5)
i = 1
for col_name in colunas_categoricas:
    plt.subplot(3,3,i)
    sbn.countplot(dados[col_name])
    i += 1

#distribution of type values
dados.groupby(['Genero']).size()

# with loop
for col_name in colunas_categoricas:
    print('-------------------------------')
    print(dados.groupby([col_name]).size())

# NUMERIC DATA

#info numeric values
dados.describe()
dados.hist(figsize=(10,10))#distribution data

import matplotlib.pyplot as plt
import seaborn as sbn

plt.figure(figsize=(20,30))
plt.subplots_adjust(hspace=0.5)
i = 1
for col_name in dados.columns.drop(colunas_categoricas):#line with columns
    plt.subplot(5,2,i)
    sbn.histplot(data=dados, x=col_name, kde=True, hue='AVC', multiple='layer', alpha=0.5, palette='viridis')
    i += 1
sbn.pairplot(data = dados, hue = "AVC")#balls

#CHECK FOR OUTLIERS WITH BOXPLOTS
#Q1=25%, Q2=50%, Q3=75%, Q3+1,5*IQR, Q1-1,5*IQR
#quartil 1, quartil 2, quartil 3, limite Superior, limite inferior

plt.figure(figsize=(30,30))
plt.subplots_adjust(hspace=0.5)

i = 1
for col_name in dados.columns.drop(colunas_categoricas):
    plt.subplot(4,4,i)
    sbn.boxplot(data=dados, y=col_name)
    i +=1

# plot one per one
sbn.boxplot(dados['Idade']).set_title('Idade')

#check nulls
dados.isnull()

# count null values 
dados.isnull().sum()

#access lines with null
dados[dados["IMC"].isnull()]

#ADJUST DATA FOR PROBLEM
# Apply o One Hot Enconding
dados_1 = pd.get_dummies(dados["Fumante"], prefix = "Fumante")
dados_1.head()

# concat data
dados_corrigidos = pd.concat([dados, dados_1], axis=1)
dados_corrigidos.head()

# transformando os dados em valores numéricos
dados_corrigidos['Genero_num'] =  dados_corrigidos['Genero'].replace({'Female': 0, 'Male': 1})
dados_corrigidos['Hipertensão_num'] =  dados_corrigidos['Hipertensão'].replace({'No': 0, 'Yes': 1})
dados_corrigidos['DoencaCoracao_num'] =  dados_corrigidos['DoencaCoracao'].replace({'No': 0, 'Yes': 1})
dados_corrigidos['JaFoiCasado_num'] =  dados_corrigidos['JaFoiCasado'].replace({'No': 0,'N' : 0,'Never' : 0,'Y' : 1,'Yes': 1})
dados_corrigidos['AVC_num'] =  dados_corrigidos['AVC'].replace({'No': 0,
                                                                'Yes': 1})
# Label Enconding:
dados_corrigidos['Sintomas_Label_Enc'] =  dados_corrigidos['Sintomas'].replace({'no symptoms ': 0,'one or two symptoms ' : 1,'three symptoms ' : 2,'four symptoms ' : 3,'five or more symptoms ': 4})
dados_corrigidos.head()

dados_corrigidos.shape#return lines,columns
dados_corrigidos.ndim #dataframe,siries
dados_corrigidos.size #

#Checando os valores em genero
dados_corrigidos.groupby(['Genero_num']).size()

#tratar os valores nulos
dados_drop = dados_corrigidos.dropna()

mediana_IMC = dados_corrigidos["IMC"].median()
mascara = dados_corrigidos["IMC"].isnull()
dados_corrigidos.fillna(mediana_IMC,inplace=True)
dados_corrigidos[mascara].head()

# Encontrando a mediana das idades
mediana_Idade = dados_corrigidos["Idade"].median()
mediana_Idade

# Criando uma mascara para selecionar os valores acima de 100 anos menores ou iguais a zero
mascara = (dados_corrigidos["Idade"] <=  0 )  | ( dados_corrigidos["Idade"] >  100)
mascara

# Checando a quantidade de valores que serão alterados.
dados_corrigidos[mascara].shape

#Tratar o outlier de idades fora do domínio
dados_corrigidos["Idade"][mascara] = mediana_Idade
dados_corrigidos[mascara].head()

# Média da coluna IMC
media_IMC = dados_corrigidos["IMC"].mean()
media_IMC

# Desvio padrão da coluna de IMC
desv_pad_IMC = dados_corrigidos["IMC"].std()
desv_pad_IMC

# Imprimindo os valores minimos e máximos
print(f"Valor minimo: {media_IMC-3*desv_pad_IMC}\nValor máximo {media_IMC+3*desv_pad_IMC}")

# Quantidade de valores abaixo ou acima de 3 desvios padrões
dados_corrigidos["IMC"][(dados_corrigidos["IMC"]< media_IMC-3*desv_pad_IMC) | (dados_corrigidos["IMC"] > media_IMC+3*desv_pad_IMC)].shape

# substituindo os valores pela mediana
dados_corrigidos["IMC"][(dados_corrigidos["IMC"]< media_IMC-3*desv_pad_IMC) | (dados_corrigidos["IMC"] > media_IMC+3*desv_pad_IMC)] = mediana_IMC

dados_corrigidos["IMC"][(dados_corrigidos["IMC"]< media_IMC-3*desv_pad_IMC) | (dados_corrigidos["IMC"] > media_IMC+3*desv_pad_IMC)].shape

dados_corrigidos.drop(columns = ["Id","Genero","Hipertensão", "DoencaCoracao", "JaFoiCasado", "Sintomas", "Fumante", "AVC"], inplace=True)
dados_corrigidos.head()

plt.figure(figsize=(12,6))
sbn.heatmap(dados_corrigidos.corr(), annot=True)

dados_corrigidos.corr()['AVC_num'].sort_values(ascending=False)

# comparar dados
# 2 medias maior e menor
# media em valores especificos
# loops
# funcoes(param)
# porcentagem de dados
#percentual de aumento em relacao a min_Column

# Adicionar novas funcoes
# Duplicar exemplos
# comentarios


