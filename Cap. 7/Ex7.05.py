# Escreva um programa que leia duas strings e gere uma terceira, 
# na qual os caracteres da segunda foram retirados da primeira

s1 = input('Digite a 1º String: ')
s2 = input('Digite a 2º String: ')

s3 = ''

for i in s1:
    if i not in s2:
        s3 += i

if s3 == '':
    print('Todos os caracteres foram removidos')
else:
    print(s3)
    