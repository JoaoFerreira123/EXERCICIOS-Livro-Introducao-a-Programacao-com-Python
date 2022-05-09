from turtle import back
from cliente import Cliente
from contas import Conta
from bancos import Banco

joao = Cliente('João da Silva', '123-456')
maria = Cliente('Maria da Silva', '789-456')

conta1 = Conta([joao], 236, 50)
conta2 = Conta([maria, joao], 542)

banco1 = Banco('Banco1')
banco1.abreConta(conta1)
banco1.abreConta(conta2)

banco1.listaContas()

conta1.saque(50)
conta2.deposito(300)
conta1.deposito(230)
conta2.saque(75)
conta1.extrato()
conta2.extrato()

conta1.resumo()