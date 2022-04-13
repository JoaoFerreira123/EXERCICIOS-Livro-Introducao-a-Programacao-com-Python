# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.



cs = float(input('Insira o valor da casa: '))
sl = float(input('Digite o seu salário: '))
a = int(input('Informe a quantidade de anos para pagar: '))

prest = cs / (12*a)
if prest > (0.3*sl):
    print(f'Empréstimo não aprovado pois a parcela de R$:{prest:.2f} excede 30% do salário')
else:
    print(f'Empréstimo aprovado! Com uma parcela de R$:{prest:.2f}')