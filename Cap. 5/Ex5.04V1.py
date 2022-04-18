# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, 
# mas, dessa vez, apenas os números ímpares.

n = int(input('Digite um número: '))
cont = 1

while cont <= n:
    if cont % 2 != 0:
        print(cont)
    cont += 1

