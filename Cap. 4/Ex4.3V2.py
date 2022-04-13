# Escreva um programa que leia três números e que imprima o maior e o menor.

num = list()

num.append(int(input('Digite o 1º número: ')))
num.append(int(input('Digite o 2º número: ')))
num.append(int(input('Digite o 3º número: ')))

print(f'O maior número é {max(num)}')
print(f'O menor número é {min(num)}')
