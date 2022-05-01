arquivo = open('teste01.txt', 'r')

for i in arquivo.readlines():
    print(i)

arquivo.close()