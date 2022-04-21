# Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou.

l = [5, 8, 7, 6, 3, 2, 9]
v = int(input('Insira o valor a procurar: '))
i = 0
while i < len(l):
    if l[i] == v:
        break
    i += 1

if i >= len(l):
    print(f'O valor {v} não foi achado')
else:
    print(f'O valor {v} foi achado na posição {i}')
