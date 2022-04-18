# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

ini = float(input('Insira o valor do Depósito Incial. R$: '))
tx = float(input('Digite a taxa de juros anual: '))
copiaini = ini
mes = 1

while mes <= 24:
    ini = ini + ((tx/12)/100)*ini
    print(f'{mes}º mês - R$:{ini:.2f}') 
    mes += 1

print(f'O total ganho com juros foi R$:{ini - copiaini:.2f}')