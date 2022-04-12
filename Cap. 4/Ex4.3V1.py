# Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
n3 = int(input('Digite o 3º Número: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor número é o {menor}')

