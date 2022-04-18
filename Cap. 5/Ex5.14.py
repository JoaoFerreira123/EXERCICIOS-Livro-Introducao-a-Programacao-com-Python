# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite O (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética

contNum = soma = 0
while True:
    n  = int(input('Digite um número (ou 0 para sair): '))
    if n == 0:
        break
    contNum += 1
    soma += n

print(f'Você digitou {contNum} números, a soma é {soma} e a média é {soma/contNum:.2f}')