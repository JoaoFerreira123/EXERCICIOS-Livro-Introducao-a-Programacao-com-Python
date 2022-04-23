# Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string

s = input('Digite a string: ')

contador = {} #um dicionário em que a chave vão ser as letras e o valor a quantidade de repetições

for letra in s:
    contador[letra] = contador.get(letra, 0) + 1 #esse +1 é o contador, pra adicionar 1 pra cada letra que seja igual a chave da letra no dicionário

for chave, valor in contador.items(): #o items retorna uma tupla com a chave e o valor do dicionarioTT
    print(f'{chave}: {valor}x')

#tem que usar o dicionário com o GET pra aparecer somente uma vez a contagem de cada letra. 