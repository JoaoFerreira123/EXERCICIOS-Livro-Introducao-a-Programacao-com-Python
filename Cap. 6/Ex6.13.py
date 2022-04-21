# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4].
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = menor = T[0]
soma = 0
for i in T:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma += i

print(f'O maior valor é {maior}, o menor é {menor} e a média é de {soma/len(T):.2f}')
