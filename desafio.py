
menu="""

Sistema Bancario


A-Deposito

B-Saque

C-Extrato

D-Sair

"""

saldo=0
limite=500
extrato = " "
n_saques=0
LIMITE_SAQUES=3

while True:
    
    opcao=input(menu)
    
    if opcao == "A":
        
        v_depostio= float(input("Digite o valor do deposito: "))
        
        if v_depostio > 0:
            
            saldo=saldo + v_depostio
            
            extrato= extrato +'Deposito: %.2f' % (v_depostio) + "\n"
            
            print("Valor Depositado com sucesso!\n")
            
        else:
            print("Valor digitado não é positivo!\n")
            
        
    elif opcao == "B":
        
        v_saque= float(input("Digite o valor do saque: "))
        
        if n_saques < 3:
            
            if v_saque <= 500 and v_saque > 0:
                
                if saldo >= v_saque:
                    
                    saldo=saldo-v_saque
                    
                    extrato= extrato +'Saque: %.2f' % (v_saque) + "\n"
                    
                    print("Saque efetuado com sucesso!")
                    
                    n_saques=n_saques+1
                    
                    
                else:
                    print("Não a saldo para esse valor de saque!")
                
            else:
                print("valor de saque acima dopermitido")
            
        else:
            print("Numeros de saque excedido!")
            
    elif opcao == "C":
        
        extrato=extrato + 'Saldo: %.2f' % (saldo)+"\n" 
        print(extrato)      
        
    elif opcao == "D":
        break
    
    else:
        print("não existe essa opção!")




