def exibir_menu():
    print('1-Consultar saldo\n0-Depósito\n3-transferência\n4-Saque\n5-Sair')

def sacar(valor):
    global saldo
    saldo -= valor 
    print(f'Saque realizado com sucesso!\n0 saldo atual da conta 290693: {saldo}')

def depositar(valor):
    global saldo
    saldo += valor 
    print(f'Depósito realizado com sucesso!\n0 saldo atual da conta 290693: {saldo} ') 

def transferir(valor):
    global saldo, destinatario
    saldo -= valor 
    destinatario += valor 
    print(f'Transferência realizada com sucesso!\n0 saldo atual da conta 290693: {saldo}')
    
while True:
    exibir_menu()
    op = int(input('Escolha uma opção'))
    if  op == 1:
        print(f'O saldo da conta 290693: {saldo_caio}')  
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        depositar(valor)

      
    elif op == 3:
        valor = float(input('Escolha o valor da transferência: '))
        transferir(valor)
        
    elif op == 4:
        valor = float(input('Escoçha o valor do saque: '))
        sacar(valor)

    
    elif op ==5:
        print('Obrigado!')
        break              
