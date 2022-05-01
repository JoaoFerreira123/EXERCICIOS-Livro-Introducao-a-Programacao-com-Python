# Crie um programa que inverta a ordem das linhas do arquivo pares.txt
# A primeira linha deve conter o maior número; e a última, o menor.

par = open('pares.txt', 'r')
parInv = open('parInv.txt', 'w')

#readlines retorna uma LISTA com as linhas
#logo é só inverter a lista
inv = par.readlines()
inv.reverse()

for i in inv:
    parInv.write(i)

par.close()
parInv.close()