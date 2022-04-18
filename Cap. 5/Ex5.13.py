# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago

vIni = float(input('Insira o valor inicial: '))
jMen = float(input('Qual é o juro mensal? '))
pagMen = float(input('Quanto será pago mensalmente? '))
divida = vIni
mes = 1

if (divida *(jMen / 100) > pagMen):
    print('Os  juros mensais são maiores que o pagamento. Você nunca vai terminar de pagar')
else: 
    totJuros = 0
    while divida > 0:
        juros = divida * (jMen/100)
        totJuros = totJuros + juros
        divida = divida + juros - pagMen
        print(f'No {mes}º mês a dívida é de R$:{divida:.2f}')
        mes += 1

    print(f'A divida será paga em {mes} meses')
    print(f'O total de JUROS pago foi de R$: {totJuros}')
