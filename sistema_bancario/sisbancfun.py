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
    
