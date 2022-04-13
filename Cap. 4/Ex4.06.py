# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, 
# e R$ 0,45 para viagens mais longas

km = float(input('Quantos KM você quer percorrer? '))

if km <= 200:
    p = 0.5*km
else:
    p = 0.45*km

print(f'Para {km}km o preço é de R$:{p:.2f}')