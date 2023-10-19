from abc import ABC, abstractclassmethod,abstractproperty
from datetime import datetime

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



class Conta:
    def __init__(self,numero,cliente):
        self._saldo=0
        self._numero=numero
        self._agencia="0001"
        self._cliente=cliente
        self._historico= Historico()
    
    @property    
    def saldo(self):
        return self._saldo
    
    @property    
    def numero(self):
        return self._numero
    
    @property    
    def agencia(self):
        return self._agencia
    
    @property    
    def cliente(self):
        return self._cliente
    
    @property    
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    def sacar(self, valor):
        saldo=self.saldo
        
        if valor > 0:
        
            if saldo >= valor:
                        
                saldo=saldo-valor
                        
                print("Saque efetuado com sucesso!")
                
                return True
                
            else:
                print("saldo insuficiente!")
                return False
        else:
            print("valor invalido para saque, favor escolher valor entre amior que 0!")
            return False
        
    
    
    def depositar(self, valor):
        saldo=self.saldo
        if  valor > 0:
                        
                saldo=saldo+valor
                        
                print("Deposito efetuado com sucesso!")
                
                return True
                
        else:
            print("valor invalido para deposito, favor escolher valor maior que 0")
            return False
                
class Cliente:
    def __init__(self, endereco):
        self.edereco=endereco
        self.contas=[]
        
    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class Pessoas_fisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.cpf=cpf
           
class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite=limite
        self.limite_saque=limite_saque
        
    def sacar(self,valor):
        n_saques=len([transacao for transacao in self.historico.transacao if transacao["tipo"]== Saque.__name__])

        if valor> self.limite:
            print("valor excedeu o limite de saque!")
            
        elif n_saques>= self.limite_saque:
            print("excedeu o limite mensal de saque!")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"Agencias: {self.agencia} \n Conta: {self.numero} \n Cliente: {self.cliente.nome}"
    
class Historico:
    def __init__(self):
        self._transacoes=[]
        
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacoes(self, transacoes):
        transacoes=self.transacoes
        transacoes.append({"tipo": transacao.__class__.__name__, "valor":transacao.valor, "data":datetime.now() })

class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor= valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        registrar_saque= conta.sacar(self.valor)
        
        if registrar_saque== True:
            conta.historico.adicionar_transacoes(self)
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor= valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        registrar_deposito= conta.depositar(self.valor)
        
        if registrar_deposito== True:
            conta.historico.adicionar_transacoes(self)
    





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
    contas=[]
    clientes=[]
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




