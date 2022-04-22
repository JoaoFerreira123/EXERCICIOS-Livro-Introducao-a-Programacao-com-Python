# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.

s1 = input('Digite a 1º String: ')
s2 = input('Digite a 2º String: ')
s3 = ''

for letra in s1:
    if letra in s2 and letra not in s3:
        s3 += letra
    
if s3 == '':
    print('Não há caracteres em comum')
else:
    print(s3)