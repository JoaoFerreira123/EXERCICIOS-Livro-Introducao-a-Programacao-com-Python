arquivo = open('teste01.txt', 'w')
for i in range(1, 101):
    arquivo.write(f'{i}\n')

arquivo.close()

