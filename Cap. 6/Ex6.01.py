# Modifique o Programa 6.2 para ler 7 notas em vez de 5.
notas = [0,0,0,0,0,0,0]

i = soma = 0
while i < 7:
    notas[i] = float(input(f'Insira a {i+1} nota: '))
    soma += notas[i]
    i += 1
media = soma/7
print(f'A média das 7 notas é {media:.2f}')

