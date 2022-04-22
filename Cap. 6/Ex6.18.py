# Escreva um programa que gere um dicionário, em que cada chave seja um caractere, 
# e seu valor seja o número desse caractere encontrado em uma frase lida

frase = input('Digite uma frase: ')
dic = {}

for i in frase:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

print(dic)

