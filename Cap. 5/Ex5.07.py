# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, 
# em vez de começar com 1 e 10

n = int(input('De qual número você quer a tabuada? '))
ini = int(input('Qual o inicio da Tabuada? '))
fim = int(input('Qual o fim da Tabuada? '))
cont = ini

while cont <= fim:
    print(f'{n} x {cont} = {n*cont}')
    cont += 1
