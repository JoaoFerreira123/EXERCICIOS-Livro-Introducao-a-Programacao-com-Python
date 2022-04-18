# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

depini = float(input('Qual o valor do depósito inicial? '))
depmen = float(input('Qual o valor depositado mensalmente? '))
tx = float(input('Qual a taxa de juros anual? '))

cont = 1
tot = depini
while cont <= 24:
    tot = tot + (((tx/12)/100) * tot) + depmen
    print(f'{cont}º mês - R$: {tot:.2f}')
    cont += 1

print(f'Em 24 meses o total ganho com juros foi R$: {tot - (depini + (depmen * 24)):.2f}') #total SÓ de juros, desconsiderando os aportes mensais e o inicial