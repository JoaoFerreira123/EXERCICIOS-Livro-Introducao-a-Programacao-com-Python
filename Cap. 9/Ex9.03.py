# Crie um programa que leia os arquivos pares.txt e ímpares.txt e que crie um só arquivo paresEImpares.txt
# com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.

#criando os arquivos
with open('pares.txt', 'w') as pares, open('impares.txt', 'w') as impares:
    for i in range(1, 1001):
        if i % 2 == 0:
            pares.write(f'{i}\n')
        else:
            impares.write(f'{i}\n')


#lendo os arquivos e concatenando 

with open('pares.txt', 'r') as pares, open('impares.txt', 'r') as impares, open('pareseImpares.txt', 'w') as pareseImpares:
    for i in range(500):
        pareseImpares.write(impares.readline())
        pareseImpares.write(pares.readline())
