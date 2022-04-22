# Escreva um programa que leia duas strings. 
# Verifique se a segunda ocorre dentro da primeira e imprima a posição de início

s1 = input('Digite a 1º String: ')
s2 = input('Digite a 2º String: ')

if s2 in s1:
    print(f'Ocorre na posição {s1.find(s2)}')
else:
    print('String não encontrada')