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
            return True
        else:
            print('Saldo Insuficiente')
            return False
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC Nº {self.numero}\n')
        for i in self.operacoes:
            print(f'{i[0]:10s} {i[1]:10.2f}')
        print(f'\n  Saldo: {self.saldo:10.2f}\n')

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        else:
            print(f'Saldo Insuficiente')
            return False

    def extrato(self):
        Conta.extrato(self) #herda os atributos da função extrato da classe Conta
        print(f'Limite Total: {self.limite}\n')
        print(f'Disponível para Saque:{self.limite + self.saldo}\n')