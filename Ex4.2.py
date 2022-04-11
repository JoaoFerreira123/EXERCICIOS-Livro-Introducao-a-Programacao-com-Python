# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

vel = float(input('Insira a Velocidade em Km/h: '))

if vel > 80:
    print(f'Você foi multado em R$:{(vel-80)*5}')
else:
    print('Não foi multado')