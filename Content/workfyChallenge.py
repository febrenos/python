#Pitch-vídeo Solicitado em PY 1:30
#https://drive.google.com/file/d/11gcMpD1kjTag70VdVuVhclh9F4XFutt3/view?usp=sharing

#video completo IBM 2:55
#https://youtube.com/watch?v=xzvzPbzUwt8&feature=share&si=EMSIkaIECMiOmarE6JChQQ

#Funções / procedimentos / listas / Tuplas / Dicionários
#BONUS: try,except / StatusCode / Validations 
connectionServer = True
StatusCode = {200:'Succes!', 400:'Bad Request', 500:'Internal Server Error'}
lstLogin = ["Lucas", "Joao", "Jeffersson"]
lstPass=["test1234","test1324", "Test3214"]
jobLst= []
history = []
menu = -1
if connectionServer:
    print(f"\nConnction Server: {StatusCode.get(200)}")# or StatusCode[200]
else:
    print(f"\nConnction Server: {StatusCode.get(500)}")

while menu != 0:
    print("\nMENU"
        ,"\n0 Stop"
        ,"\n1 Login"#adm / candidato / recrutador
        ,"\n2 Register"#candidato / recrutador
        ,"\n3 Create job"#recrutador
        ,"\n4 Register in job"#candidato
        ,"\n5 Show users"#adm
        ,"\n6 Show history"#adm
        ,"\n7 Delete an user"#adm
        ,"\n8 Search job"#adm / candidato
        ,"\n9 Show jobs")#adm / candidato
    menu = int(input("Type one: "))

    #adm / candidato / recrutador
    if menu == 1:
        print("\nLOGIN USER")
        compareLogin = input("Login: ")
        comparePass = input("Password: ")
        def loginUser(login,password):
            valid = "fail"
            cont = 0
            while cont < len(lstLogin)-1:
                if login == lstLogin[cont]:
                    if password == lstPass[cont]:
                        print(f"\nStatus Code: {StatusCode.get(200)}")
                        print("Welcome "+ login)
                        tupla = (f"LOGIN {login}")
                        history.append(tupla)
                        valid = "ok"
                cont += 1
            if valid == "fail":
                print(f"\nStatus Code: {StatusCode.get(400)}")
        loginUser(compareLogin,comparePass)

    # candidato / recrutador
    if menu == 2:
        print("\nREGISTER USER")
        userName = input("Seu nome Completo: ")
        login = input("Login: ")
        while login in lstLogin:
            login = input("Login: ")
        lstLogin.append(login)
        password = input("Senha: ")
        # valid pass
        isLower,isUpper,isDigit,sCharacter = 0,0,0,0
        while isLower == 0 or isUpper==0 or isDigit == 0 or sCharacter == 0:
            isLower,isUpper,isDigit,sCharacter = 0,0,0,0
            if (len(password) >= 8):
                for i in password: 
                    if i.islower():
                        isLower += 1
                    if i.isupper():
                        isUpper += 1
                    if i.isdigit():
                        isDigit += 1
                    if i=="@" or i=="$" or i=="_" or i =="#" or i =="!" or i=="%" or i=="*":
                        sCharacter += 1
            if isLower<1 or isUpper<1 or isDigit<1 or sCharacter<1:
                print("\nINVALID PASSWORD \nThis need lowercase, more than 7 characters upercase and content one of this characters: @,$,_,#,!,%,*")
                password = input("Password: ")
        if isLower>0 and isUpper>0 and isDigit>0 and sCharacter>0:
            print("\nPASSWORD IS VALID")

        confirmPassword = input("Confirm pass: ")
        while confirmPassword != password:
            print("Passwords are differents")
            confirmPassword = input("Confirm pass: ")
        if confirmPassword == password:
            print("Passwords are the same!")
            lstPass.append(password)
        #valid email
        email = input("E-mail: ")
        def validEmail(e):
            character1,character2 = 0,0
            while character1 == 0 and character2 == 0:
                character1,character2 = 0,0
                for i in e:
                    if i=="@":
                        character1 += 1
                    if i==".":
                        character2 += 1
                if character1 != 1 or character2 == 0:
                    print("\nInvalid E-mail")
                    e = input("E-mail: ")
                if character1 == 1 and character2 > 0:
                    print("\nEmail is valid")
                    break
        validEmail(email)
        cpf = int(input("cpf: "))
        candidateOrRecruiter = bool(input("Candidate(False) or Recruiter(True): "))
        bornIn = input("Born in: ")

        haveCompany = int(input("Digite 1 caso trabalhe, \ndigite outra tecla caso nao: "))
        if haveCompany == 1:
            NomeEmpresaAtual = input("Digite o nome da empresa atual: ")
            cnpjEmpresaAtual = int(input("Digite o cnpj da empresa atual: "))
        else:
            NomeEmpresaAtual = "NONE"
            cnpjEmpresaAtual = "NONE"
        active = True
        try:
            lstLogin.append(userName)
            tupla = (f"REGISTER {login}")
            history.append(tupla)
            
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")
    if menu == 3:
        print("\nCREATE JOB")
        titleJob = input("Title Job: ")
        description = input("Description: ")
        typeDev =  input("Type Development: ")
        technologies =  input("Technologies: ")
        try:
            jobLst.append((titleJob,description,typeDev,technologies))
            tupla = (f"NEW JOB {titleJob}")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 4:
        print("\nREGISTER IN JOB")
        about = input("Talk about you: ")
        print("Send us an e-mail!")
        try:
            tupla = (f"REGISTED IN JOB")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 5:
        print("\nSHOW USERS")
        print(lstLogin)
        try:
            tupla = ("SHOW USERS")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 6:
        print("\nSHOW HISTORY")
        print(history)        
        try:
            tupla = ("SHOW HISTORY")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 7:
        print("\nDELETE AN USER")
        deleteUser = input("Adm, type an user for remove: ")
        def deleteUSer(u, l):#user, list
            if u in l:
                l.remove(u)
                print(f"The User {u} was deleted")
                print(l)
                tupla = (f"{u} DELETED")
                history.append(tupla)
            else:
                print(f"The user {u} not found")
                print(l)
                tupla = (f"{u} FAIL TO DELETED")
                history.append(tupla)
        try:
            deleteUSer(deleteUser, lstLogin)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 8:
        print("\nBUSCA VAGA")
        searchJob = input("Name job for search: ")
        try:
            tupla = ("BUSCA VAGA")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")

    if menu == 9:
        print("\nVIZUALIZAR VAGAS")
        print(jobLst)
        try:
            tupla = ("VIZUALIZAR VAGA")
            history.append(tupla)
        except:
            print(f"\nStatus Code: {StatusCode.get(400)}")
        else:
            print(f"\nStatus Code: {StatusCode.get(200)}")