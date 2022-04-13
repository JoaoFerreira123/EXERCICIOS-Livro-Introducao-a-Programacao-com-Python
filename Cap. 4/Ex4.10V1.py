# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir. (tabela pg 82)

qtde = float(input('Quantos KWh foram consumidos? '))
print('\nR para RESIDÊNCIAS\nI para INDÚSTRIAS\nC para COMÉRCIOS\n')
tipo = input('Qual o tipo de instalação? ')

if tipo == 'R':
    if qtde <= 500:
        valor = qtde * 0.4
    else:
        valor = qtde * 0.65
elif tipo == 'C':
    if qtde <= 100:
        valor = qtde * 0.55
    else:
        valor = qtde * 0.6
elif tipo == 'I':
    if qtde <= 5000:
        valor = qtde * 0.55
    else:
        valor = qtde * 0.6
else:
    print('Tipo Inválido')

print(f'O valor a ser pago é de R$: {valor}')