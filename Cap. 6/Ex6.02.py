# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras

from numpy import intp


x1 = x2 = i = j = 0
l1 = []
l2 = []

t1 = int(input('Insira o tamanho da Lista 1: '))
t2 = int(input('Insira o tamanho da Lista 2: '))

while i < t1:
    l1.append(int(input(f'Insira o {i+1}º elemento da lista 1: ')))
    i += 1

while j < t2:
    l2.append(int(input(f'Insira o {j+1}º elemento da lista 2: ')))
    j += 1

l3 = l1 + l2
print(l3)