arquivo = open('C:/Users/joaoa/Desktop/Programação/Python/EXERCÍCIOS - Livro Introdução a Programação com Python/Cap. 9/teste01.txt', 'r')
#só funcionou colocando todo o path, mesmo estando na mesma pasta
for i in arquivo.readlines():
    print(i)

arquivo.close()