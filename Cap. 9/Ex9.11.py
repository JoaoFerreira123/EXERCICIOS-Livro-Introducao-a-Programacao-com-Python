# Crie um programa que leia um arquivo e crie um dicionário 
# em que cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.

arq = input('Insira o arquivo: ')
arquvo = open(arq, 'r')
cont = dict()

for i in arquvo.readlines(): #linhas
    i = i.lower().strip() #letra minuscula e tira os espaços
    palavras = i.split() # i é uma string, o split transforma numa lista 
    for j in palavras:
        if j in cont: #se a palavra já estiver no dic, só conta
            cont[j] += 1
        else: #se não tiver, adiciona 
            cont[j] = 1
arquvo.close()

for i in cont:
    print(f'{i} = {cont[i]}')