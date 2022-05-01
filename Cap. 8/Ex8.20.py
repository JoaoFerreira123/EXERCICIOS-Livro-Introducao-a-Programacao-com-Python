# Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número. 
# O programa termina se o usuário acertar ou errar três vezes

from random import randint
i = 0
while i < 3:
    num = randint(1, 10)
    n = int(input('Insira um número: '))
    if n == num:
        print('Parabéns, Acertou!')
    else:
        print('Errou')
    i+=1