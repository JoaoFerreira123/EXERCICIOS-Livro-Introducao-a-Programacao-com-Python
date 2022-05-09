class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abreConta(self, conta):
        self.contas.append(conta)
    
    def listaContas(self):
        for i in  self.contas:
            i.resumo()

            