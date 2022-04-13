# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada

print('-'*20)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
print('-'*20)
print('+ -> soma\n- -> Subtração\n* -> Multiplicação\n/ -> Divisão')
op = input('Insira qual operação você quer realizar: ')
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1/n2)
else:
    print('Operação Inválida')