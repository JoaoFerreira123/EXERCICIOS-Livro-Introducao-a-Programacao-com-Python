# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
cont = 0
mult = 0
while cont < n2:
    mult = mult + n1
    cont += 1

print(f'{n1} x {n2} = {mult}')