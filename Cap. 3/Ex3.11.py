# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.
valor = float(input('Insira o preço: '))
desc = float(input('Insira o percentual de desconto: '))

print(f'O produto de R$:{valor} com {desc}% de desconto fica em R$:{valor-((desc/100)*valor)}')