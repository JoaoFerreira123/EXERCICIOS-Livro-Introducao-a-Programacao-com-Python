# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, de 15%

s = float(input('Insira o salário: '))
if s > 1250:
    s = (0.1*s) + s
else:
    s = (0.15*s) + s

print(F'Com aumento, o salário ficou R$:{s}')