# Modifique o exemplo para pesquisar dois valores. 
# Em vez de apenas p, leia outro valor v que também será procurado. 
# Na impressão, indique qual dos dois valores foi achado primeiro.
# Indique também a posição que os valores foram achados

l = [5, 8, 7, 6, 3, 2, 9]
v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))
achouV1 = -1
achouV2 = -1
i = 0
while i< len(l):
    if l[i] == v1:
        achouV1 = i
    if l[i] == v2:
        achouV2 = i
    i+=1

if achouV1 != -1:
    print(f'Valor {v1} encontrado na posição {achouV1}')
else:
    print(f'Valor {v1} não encontrado')
if achouV2 != -1:
    print(f'Valor {v2} encontrado na posição {achouV2}')
else:
    print(f'Valor {v2} não encontrado')


if achouV1 != -1 and achouV2 != -1:
    if achouV1 >= achouV2:
        print(f'{v2} foi achado primeiro')
    else:
        print(f'{v1} foi achado primeiro')