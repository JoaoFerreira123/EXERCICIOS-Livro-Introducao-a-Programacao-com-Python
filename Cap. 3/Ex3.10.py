# sFaça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.
salario = float(input('Insira o salário: '))
aumento = float(input('Insira a porcentagem de aumento: '))

print(f'O salário com um aumento de {aumento}% ficou R%: {(salario*(aumento/100)+salario)}')