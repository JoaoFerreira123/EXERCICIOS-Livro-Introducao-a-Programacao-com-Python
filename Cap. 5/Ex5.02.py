#Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
#  O programa deve imprimir 10, 9, 8, ... , 1, O e Fogo! na tela.

from time import sleep

t = 10

while t >= 0:
    print(t)
    sleep(1)
    t -= 1
print('Fogoo!')