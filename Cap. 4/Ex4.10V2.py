# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir. (tabela pg 82)


qtde = float(input('Quantos KWh foram consumidos? '))
print('\nR para RESIDÊNCIAS\nI para INDÚSTRIAS\nC para COMÉRCIOS\n')
tipo = input('Qual o tipo de instalação? ')
v = 0
match tipo:
    case 'Rr':
        if qtde > 500:
            v = qtde * 0.65
        else:
            v = qtde * 0.4
    case 'Cc':
        if qtde > 1000:
            v = qtde * 0.6
        else:
            v = qtde * 0.55
    case 'Ii':
        if qtde > 5000:
            v = qtde * 0.6
        else:
            v = qtde * 0.55

print(f'O valor a ser pago é de R$: {v}')