# Escreva um programa que receba o nome de um arquivo pela linha de comando 
# e que imprima todas as linhas desse arquivo.


name = input('Digite o nome do arquivo: ')

arquivo = open(name, 'r')

for i in arquivo.readlines():
    print(i)

arquivo.close()

#também é possível fazer com o sys, executando o programa e passando os parâmetros pelo terminal
