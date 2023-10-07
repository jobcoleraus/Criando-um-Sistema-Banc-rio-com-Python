
menu="""

Sistema Bancario


A-Deposito

B-Saque

C-Extrato

D-Criar Uuario

E-Criar Conta

F-Listar Usuarios

G-Listar Contas

H-Sair

"""

saldo=0
limite=500
extrato = " "
n_saques=0
LIMITE_SAQUES=3
AGENCIA="0001"
conta=0
list_usuario=list()
list_contas=list()


def saque(sald=saldo, lim=limite, ext=extrato, n_saq=n_saques, lim_saq=LIMITE_SAQUES, valor=0):
    
    if n_saq < lim_saq:
            
        if v_saque <= 500 and v_saque > 0:
                
            if sald >= v_saque:
                    
                saldo=sald-v_saque
                    
                extrato= ext +'Saque: %.2f' % (v_saque) + "\n"
                    
                print("Saque efetuado com sucesso!")
                    
                n_saques=n_saq+1
                    
                    
            else:
                print("Não a saldo para esse valor de saque!")
                saldo=sald
                extrato=ext
                n_saques=n_saq
                
        else:
            print("valor de saque acima do permitido")
            saldo=sald
            extrato=ext
            n_saques=n_saq
            
    else:
        print("Numeros de saque diario excedido!")
        saldo=sald
        extrato=ext
        n_saques=n_saq
        
    return saldo, extrato, n_saques

def deposito(sald,ext,valor):
    
    if v_deposito > 0:
            
        saldo=sald + v_deposito
            
        extrato= ext +'Deposito: %.2f' % (v_deposito)+ "\n"
            
        print("Valor Depositado com sucesso!\n")
            
    else:
        print("Valor digitado não é positivo!\n")
        saldo=sald
        extrato=ext
    
    return saldo,extrato
    
def extrat(sald,ext=extrato):
    
    extrato=ext + 'Saldo: %.2f' % (saldo)+"\n" 
    print(extrato)
    
    return

def criar_usuario(lista=list_usuario,nom="",nascimento="",CPF="", ende=""):
    
    existe_usuario=0
    dic=dict()
    if len(lista) ==0:
        dic["nome"]=nome
        dic["nascimento"]=nasc
        dic["CPF"]=cpf
        dic["endereco"]=endereco
        
        print(dic)
        
        lista.append(dic)
        list_usuario= lista
        print("Usuario criado com sucesso!")

    else:
        dic["nome"]=nome
        dic["nascimento"]=nasc
        dic["CPF"]=cpf
        dic["endereco"]=endereco
        
        for i in lista:
            cpf_atual=dic["CPF"]
            cpf_usuarios=i['CPF']
            if cpf_atual==cpf_usuarios:
                existe_usuario=1
        if  existe_usuario==1:
            print("Usuario ja cadastrado!") 
            list_usuario=lista         
        else:
            lista.append(dic)
            list_usuario= lista
            print("Usuario criado com sucesso!")
    return list_usuario
     
def criar_conta(list_usu=list_usuario,list_cont=list_contas,CPF_usuario=0, cont=conta):
    existe_usuario=0
    global AGENCIA
    dic=dict()
    if len(list_usu)==0:
        print("não ha usuarios cadastrados, favor cadastrar um usuario para criar a conta!")
        list_contas=list_cont
        conta=cont
    else:
        for i in list_usu:
            cpf_usuarios=i['CPF']
            if cpf_usu==cpf_usuarios:
                existe_usuario=1
        if existe_usuario==1:
            conta=cont+1
            dic["agencia"]=AGENCIA
            dic["conta"]=conta
            dic["CPF_usuario"]=cpf_usu
            list_cont.append(dic)
            list_contas= list_cont
            print("Conta criada com sucesso!")
        else:
            list_contas=list_cont
            conta=cont
            print("Usuario não cadastrado, favor cadastrar usuario ante de criar conta!") 
    return list_contas, conta

while True:
    
    opcao=input(menu)
    
    if opcao == "A":#Deposito
        
        v_deposito= float(input("Digite o valor do deposito: "))
        
        tupla_deposito=deposito(saldo,extrato,v_deposito)
        saldo=tupla_deposito[0]
        extrato=tupla_deposito[1]
    
        
    elif opcao == "B":#Saque
        
        v_saque= float(input("Digite o valor do saque: "))
        
        tupla_saque=saque(sald=saldo, lim=limite, ext=extrato, n_saq=n_saques, lim_saq=LIMITE_SAQUES, valor=v_saque)
        saldo=tupla_saque[0]
        extrato=tupla_saque[1]
        n_saques=tupla_saque[2]
        
            
    elif opcao == "C":#extrato
        
        extrat(saldo,ext=extrato)
        
    elif opcao == "D":#criar usuario
        nome=str(input("Digite o nome do usuario: "))
        nasc=str(input("Digite a data do nascimento do usuario: "))
        cpf=str(input("Digite o CPF do usuario(somente os numeros): "))
        endereco=str(input("Digite o endereço do usurario(formato:logradouro-num-bairro-cidade/sigla estado): "))

        list_usuario=criar_usuario(lista=list_usuario,nom=nome,nascimento=nasc,CPF=cpf, ende=endereco)
        print(type(list_usuario))
        print(list_usuario)
    elif opcao == "E":#criar conta
        cpf_usu=str(input("Digite o CPF do usuario que deseja criar a conta(somente os numeros): "))
        
        tupla_conta=criar_conta(list_usu=list_usuario,list_cont=list_contas,CPF_usuario=cpf_usu, cont=conta)
        list_contas=tupla_conta[0]
        conta=tupla_conta[1]
        
    elif opcao == "F":#Listar usuarios
        for i in list_usuario:
            print(i)
    
    elif opcao == "G":#listar contas
        for i in list_contas:
            print(i)
        
    elif opcao == "H":#sair
        break
    
    else:
        print("não existe essa opção!")




