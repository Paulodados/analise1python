class ContaCorrente:
    def __init__(self, senha, num_conta, saldo = 0.0):
        self.num_conta = num_conta
        self .saldo = saldo
        self.senha = senha

    def consultar_saldo(self):
        print(f' O saldo da conta {self.num_conta}: R$ {self.saldo:.2f}')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor 
            print(f'Saque realizado com sucesso!\n0 saldo atual da conta {self.num_conta} : {self.saldo}')
        else:
            print(' Saldo insuficiente ou inválido! ')    
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor 
            print(f'Depósito realizado com sucesso!\n0 saldo atual da conta {self.num_conta}: {self.saldo:.2f} ')
        else:
            print(' Opeeação inválida')    

    def transferir(self, destinatario, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor 
            print(f'Saque realizado com sucesso!\n0 saldo atual da conta {self.num_conta} : {self.saldo}')
        else:
            print(' Saldo insuficiente ou inválido! ')    
         
    