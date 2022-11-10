# INTEGRANTES
# RM94266 Vinicius Alves Torres
# RM94513 Leandro Alves de Souza Braga
# RM92895 Vinicius Yuji Nishioka
# RM94170 Felipe Breno Sugisawa Altran
# RM93187 Gabriel Joao da Silva

# SOLICITADO(feito)
# Tuplas, Algoritimos de regressao, lst, if, loops, dicionario

# BONUS(feito)
# validador de data
# 4 + 6 menus
# escrever em TXT
# editor
# passar de meses para anos
# ...

print("\nPROBLEMA")
print("\n3.6 Até 2020, reduzir pela metade as mortes e os ferimentos,"
        ,"\nglobais por acidentes em estradas. No Brasil, em 2015 ocorreu" 
        ,"\n19 mortes de trânsito para cada 100 mil habitantes. Em 2019,"  
        ,"\na taxa reduziu para 15 mortes para cada 100 mil habitantes,"
        ,"\nmas ainda longe da meta da ODS.\n")
lstRecordMonth =[   {"mesAnoReferencia":"10-2021", "totalHabitantes": 20000, "totalObitos": 5000}
                     ,{"mesAnoReferencia":"09-2021", "totalHabitantes": 20000, "totalObitos": 3000}
                     ,{"mesAnoReferencia":"08-2021", "totalHabitantes": 19000, "totalObitos": 2000}
                     ,{"mesAnoReferencia":"09-2019", "totalHabitantes": 19000, "totalObitos": 2000}
                     ,{"mesAnoReferencia":"07-2019", "totalHabitantes": 20000, "totalObitos": 1000}
                     ,{"mesAnoReferencia":"06-2019", "totalHabitantes": 20500, "totalObitos": 1100}
                     ,{"mesAnoReferencia":"06-2020", "totalHabitantes": 20000, "totalObitos": 1100}
                     ,{"mesAnoReferencia":"07-2020", "totalHabitantes": 23000, "totalObitos": 900}
                     ,{"mesAnoReferencia":"08-2020", "totalHabitantes": 21500, "totalObitos": 1000}]
lstRecordYear = []
years = ["2022","2021","2020","2019"]#required
history = []
connectionServer = True
StatusCode = {200:"Succes!", 400:"Bad Request", 500:"Internal Server Error"}

def actualizeRecordYear():
    lstRecordYear = []
    for y in years:
        c = 0
        lstFilter = []
        while c in range(len(lstRecordMonth)):
            strMonth = str(lstRecordMonth[c]["mesAnoReferencia"][3:7])
            if strMonth == y:
                lstFilter.append(lstRecordMonth[c])
            c+=1
        if len(lstFilter) != 0:
            c = 0
            Deaths = 0
            inhabitant = 0
            while c in range(len(lstFilter)):
                inhabitant += lstFilter[c]["totalHabitantes"]
                Deaths += lstFilter[c]["totalObitos"]
                c+=1
            DRecord = {"mesAnoReferencia":y, "totalHabitantes": inhabitant, "totalObitos": Deaths}
            # DRecord = {"mesAnoReferencia":y, "totalHabitantes": inhabitant//len(lstFilter), "totalObitos": Deaths//len(lstFilter)}
            lstRecordYear.append(DRecord)
    return lstRecordYear

# valid DT
def validDT(value):
    c = 0
    if len(value) == 7:
        for i in str(value):
            if c != 2 and not i.isnumeric():
                return False
            if value[2] != "-":
                return False
            c += 1
    else:
        return False
    if int(value[0:2]) < 1 or int(value[0:2]) > 12:
        print(">>> mes invalido")
        return False
    if int(value[3:7]) < 1912 or int(value[3:7]) > 2022:
        print(">>> ano invalido")
        return False
    return True

#order an list
def selectionSort(lst, i):
    pos_menor = i 
    i = i + 1
    while i < len(lst):
        if int(lst[pos_menor]) > int(lst[i]):
            pos_menor = i
        i = i + 1
    return pos_menor

if connectionServer:
    print(f"\nConnction Server: {StatusCode.get(200)}")# or StatusCode[200]
    menu=-1
    while menu != 0:
        print("\nMENU"
        ,"\n0 Stop"
        ,"\n1 Cadastrar mes Referencia"
        ,"\n2 Exibir dados do mês de referência [pesquisa por mês]"
        ,"\n3 Relatório comparativo – ano"
        ,"\n4 Relatório comparativo – mes"
        ,"\n5 Listar todos os mes(es) cadastrados"
        ,"\n6 Listar todos os ano(s) cadastrados"
        ,"\n7 Editar Registro"
        ,"\n8 Salvar em TXT"
        ,"\n9 Ver Historico"
        ,"\n10 Ordenar anos")
        menu = int(input("Opcao menu: "))

        referencialDay = 0
        inhabitant = 0
        Deaths = 0
        if menu == 1:
            print("\nREGISTRAR")
            referencialDay = input("Mes, ano referencia (MM-YYYY): ")
            while not validDT(referencialDay):
                print(">>> Formato invalido")
                referencialDay = input("Mes, ano referencia (MM-YYYY): ")
            inhabitant = int(input("Total habitantes: "))
            Deaths = int(input("Total de mortes: "))
            DRecord = {"mesAnoReferencia":referencialDay, "totalHabitantes": inhabitant, "totalObitos": Deaths}
            lstRecordMonth.append(DRecord)
            print(f"Status Code: {StatusCode.get(200)}")
            tupla = (f"REGISTRAR {referencialDay}")
            history.append(tupla)
            print(f">>> REGISTRADO {referencialDay}")

        if menu == 2:
            print("\nEXIBIR DADOS DO MES")
            month = input("Mes: ")
            c = 0
            lstFilter = []
            while c in range(len(lstRecordMonth)):
                if month == lstRecordMonth[c]["mesAnoReferencia"][0:2]:
                    lstFilter.append(lstRecordMonth[c])
                c+=1
            if len(lstFilter) > 0:
                c = 0
                for i in lstFilter:
                    print(f"{c}. {i}")
                    c+=1
                print(">>> Encontrado!")
                print(f"Status Code: {StatusCode.get(200)}")
            else:
                print(">>> Mês-ano não cadastrado!")
                print(f"Status Code: {StatusCode.get(400)}")
            tupla = (f"DADOS DO MES")
            history.append(tupla)

        if menu == 3:
            print("\nRELATORIO COMPARATIVO ANO")
            lstRecordYear = []
            for y in years:
                c = 0
                lstFilter = []
                while c in range(len(lstRecordMonth)):
                    strMonth = str(lstRecordMonth[c]["mesAnoReferencia"][3:7])
                    if strMonth == y:
                        lstFilter.append(lstRecordMonth[c])
                    c+=1
                if len(lstFilter) != 0:
                    c = 0
                    Deaths = 0
                    inhabitant = 0
                    while c in range(len(lstFilter)):
                        inhabitant += lstFilter[c]["totalHabitantes"]
                        Deaths += lstFilter[c]["totalObitos"]
                        c+=1
                    DRecord = {"mesAnoReferencia":y, "totalHabitantes": inhabitant, "totalObitos": Deaths}
                    lstRecordYear.append(DRecord)
            print("\nMORTALIDADE ANUAL")
            if len(lstRecordYear) > 1:
                c = 0
                for i in lstRecordYear:
                    print(f"{c}. {i}")
                    c+=1
                print("Dois itens para analise:")
                i1 = int(input("index item 1: "))
                i2 = int(input("index item 2: \n"))
                try:
                    #if lstRegistro lista anos
                    v1 = (lstRecordYear[i1]["totalObitos"]/lstRecordYear[i1]["totalHabitantes"]*100)
                    v2 = (lstRecordYear[i2]["totalObitos"]/lstRecordYear[i2]["totalHabitantes"]*100)
                    print(i1,": totalObitos / totalHabitantes: ", "%.2f" % (v1), "% death(s)")
                    print(f"{i1} : {lstRecordYear[i1]}\n")
                    print(i2, ": totalObitos / totalHabitantes: ", "%.2f" % (v2), "% death(s)")
                    print(f"{i2} : {lstRecordYear[i2]}")
                    if v1 < v2:
                        print(i1, "e", "%.2f" % (v2-v1), " % menor que", i2)
                    elif v1 == v2:
                        print(i1, "e", i2, "possuem taxa iguais")
                    else:
                        print(i2, "possui taxa de", "%.2f" % (v1-v2), "% menor que", i1)
                    print(f"\nStatus Code: {StatusCode.get(200)}")
                except:
                    print(">>> Exeption to get index")
                    print(f"Status Code: {StatusCode.get(400)}")
                
            else:
                print(">>> minimo 2 valores na lista ANOS")
                print(f"Status Code: {StatusCode.get(400)}")
            tupla = (f"RELATORIO ANO")
            history.append(tupla)

        if menu == 4:
            print("\nRELATORIO COMPARATIVO MES")
            if len(lstRecordMonth) > 1:
                c = 0
                for i in lstRecordMonth:
                    print(f"{c}. {i}")
                    c+=1
                print("Dois itens para analise:")
                i1 = int(input("item 1: "))
                i2 = int(input("item 2: \n"))
                try:
                    print("\nMORTALIDADE MENSAL")
                    v1 = (lstRecordMonth[i1]["totalObitos"]/lstRecordMonth[i1]["totalHabitantes"]*100)
                    v2 = (lstRecordMonth[i2]["totalObitos"]/lstRecordMonth[i2]["totalHabitantes"]*100)
                    
                    print(i1,": totalObitos / totalHabitantes: ", "%.2f" % (v1), "% death(s)")
                    print(f"{i1} : {lstRecordMonth[i1]} \n")
                    print(i2,": totalObitos / totalHabitantes: ", "%.2f" % (v2), "% death(s)")
                    print(f"{i2} : {lstRecordMonth[i2]}")
                    if v1 < v2:
                        print(i1, "e", "%.2f" % (v2-v1), " % menor que", i2)
                    elif v1 == v2:
                        print(i1, "e", i2, "possuem taxa iguais")
                    else:
                        print(i2, "possui taxa de", "%.2f" % (v1-v2), "% menor que", i1)
                    print(f"\nStatus Code: {StatusCode.get(200)}")
                except:
                    print(">>> Exeption to get index")
                    print(f"Status Code: {StatusCode.get(400)}")
            else:
                print(">>> minimo 2 valores na lista")
                print(f"Status Code: {StatusCode.get(400)}")
            tupla = (f"RELATORIO MES")
            history.append(tupla)

        if menu == 5:
            print("\nLISTAR MESES CADASTRADOS")
            c=0
            for i in lstRecordMonth:
                print(f"{c}. {i}")
                c+=1
            tupla = (f"LISTAR MES(ES)")
            history.append(tupla)

        if menu == 6:
            print("\nLISTAR ANO(S) CADASTRADOS")
            c = 0
            for i in actualizeRecordYear():
                    print(f"{c}. {i}")
                    c+=1
            tupla = (f"LISTAR ANO(S)")
            history.append(tupla)

        if menu == 7:
            print("\nEDITAR REGISTRO")
            c = 0
            for i in lstRecordMonth:
                    print(f"{c}. {i}")
                    c+=1
            editItem = int(input("Index do item: "))
            print("\n0 mesAnoReferencia"
            ,"\n1 totalHabitantes"
            ,"\n2 totalObitos")
            keyEdit = int(input("Selecione a chave: "))
            if editItem >= 0 and editItem <= len(lstRecordMonth):
                if keyEdit == 0:
                    valueEdit = input("Mes, ano referencia (MM-YYYY): ")
                    while not validDT(valueEdit):
                        valueEdit = input("Mes, ano referencia (MM-YYYY): ")
                    lstRecordMonth[editItem]["mesAnoReferencia"] = valueEdit
                    print(f"Status Code: {StatusCode.get(200)}")
                elif keyEdit == 1:
                    valueEdit = int(input("Selecione o valor: "))
                    lstRecordMonth[editItem]["totalHabitantes"] = valueEdit
                    print(f"Status Code: {StatusCode.get(200)}")
                elif keyEdit == 2:
                    valueEdit = int(input("Selecione o valor: "))
                    lstRecordMonth[editItem]["totalObitos"] = valueEdit
                    print(f"Status Code: {StatusCode.get(200)}")
                else:
                    print(">>> Erro index")
                    print(f"Status Code: {StatusCode.get(400)}")
            tupla = (f"EDITAR REGISTRO")
            history.append(tupla)

        if menu == 8:
            print("\nSALVAR EM TXT")
            registroTxt = open("registro.txt", "w")
            registroTxt.write("MEDIA REGISTRO DE ANO(S)\n")
            c=0
            for i in actualizeRecordYear():
                registroTxt.write(f"{c}. {i}\n")
                c+=1
            registroTxt.write("REGISTRO DE MES(ES)\n")
            c=0
            for i in lstRecordMonth:
                registroTxt.write(f"{c}. {i}\n")
                c+=1
            
            registroTxt.close()
            print(">>> registrado em TXT")
            print(f"Status Code: {StatusCode.get(200)}")
            tupla = (f"REGISTRO EM TXT")
            history.append(tupla)

        if menu == 9:
            print("\nVER HISTORICO")
            tupla = (f"VER HISTORICO")
            history.append(tupla)
            print(history)
        if menu == 10:
            print("\nORDENAR ANOS")
            for i in range(len(years)):
                j = selectionSort(years, i)
                aux = years[j]
                years[j] = years[i]
                years[i] = aux
            print("\n",years)
            print(">>> Selection Sort")
            print(f"Status Code: {StatusCode.get(200)}")
            tupla = (f"ORDENAR ANOS")
            history.append(tupla)
else:
    print(f"\nConnction Server: {StatusCode.get(500)}")