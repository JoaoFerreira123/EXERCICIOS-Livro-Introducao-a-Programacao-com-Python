class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f'CC Número: {self.numero} - Saldo: {self.saldo:10.2f}')
        for i in self.clientes:
            print(f'Nome: {i.nome} - Telefone: {i.telefone}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print('Saldo Insuficiente')
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC Nº {self.numero}\n')
        for i in self.operacoes:
            print(f'{i[0]:10s} {i[1]:10.2f}')
        print(f'\n  Saldo: {self.saldo:10.2f}\n')
