# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input('Digite quantos KM foram rodados: '))
d = int(input('Digite quantos dias o carro foi alugado: '))

valor = (km * 0.15) +  (60 * d)
print(f'O valor a pagar é de R$: {valor}')