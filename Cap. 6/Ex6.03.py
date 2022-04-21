# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
l1 = [5, 8, 9, 7, 8]
l2 = [2, 4, 3, 2, 6]

l3 = list(set(l1 + l2)) #o método SET retorna a união de duas listas sem repetição

print(l3)
