#Crie um programa que receba uma lista de nomes de arquivo e os imprima, um por um.

arquivos = list()

while True:
    txt = input('Insira o nome do arquivo: (0 para parar): ')
    if txt == '0':
        break
    else:
        arquivos.append(txt)
    
for i in arquivos:
    arq = open(i, 'r')
    for j in arq:
        print(j, end = '')

arq.close()