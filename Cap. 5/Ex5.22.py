# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
# Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida


print('+ -> soma\n- -> subtracao\n* -> multiplicacao\n/ -> divisao\n0 -> sair')
while True:
    x = 0
    op = input('Insira uma opção: ')
    num = int(input('Insira o número: '))
    if op == '0':
        break
    elif op in '+-*/':
        while x <=10:
            if op ==  '+':
                print(f'{num} + {x} = {num+x}')
            if op == '-':
                print(f'{num} - {x} = {num-x}')
            if op == '*':
                print(f'{num} x {x} = {num*x}')
            if op == '/':
                print(f'{num} / {x} = {num/x}')
            x += 1
    else:
        print('Opção Inválida')