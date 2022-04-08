#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salario = float(input('Qual é o seu salário: '))

if salario > 1200:
    print('Tem que pagar Imposto!')
else:
    print('Não tem que pagar Imposto!')