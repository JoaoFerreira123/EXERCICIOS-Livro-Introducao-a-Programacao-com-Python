# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem

dist = float(input('Insira a distância em KM: '))
vel = float(input('Insira a velocidade média em KM/H: '))

print(f'A viagem levará {dist/vel}h')