

conta_caio = 290693 
saldo_caio = '50.000.00'
titular = 'Caio'
print(f'{titular} - conta número 290693 - saldo atual: R$ {saldo_caio} ')

conta_catia = 201170
saldo_catia = '75.000.00'
titular = 'Catia'

while True:
    print('1-Consultar saldo\n2-Depósto\n3-Transferência\n4-Saque\n5-Sair')
    op = int(input('Escolha uma opção'))
    if  op == 1:
        print(f'O saldo da conta 290693: {saldo_caio}')  
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        saldo_caio += valor 
        print(f'Depósito realizado com sucesso!\n0 saldo atual da conta 290693: {saldo_caio} ')
    elif op == 3:
        valor = float(input('Escolha o valor da transferência: '))
        saldo_caio -= valor 
        saldo_catia += valor 
        print(f'Transferência realizada com sucesso!\n0 saldo atual da conta 290693: {saldo_caio}')
    elif op == 4:
        valor = float(input('Escoçha o valor do saque: '))
        saldo_caio -= valor 
        print(f'Saque realizado com sucesso!\n0 saldo atual da conta 290693: {saldo_caio}')
    elif op ==5:
        print('Obrigado!')
        break              
