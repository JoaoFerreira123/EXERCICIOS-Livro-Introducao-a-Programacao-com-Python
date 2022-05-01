# Crie um programa que receba uma lista de nomes de arquivo e que gere apenas um grande arquivo de saída
arquivos = list()
saida = open('saidaGrande.txt', 'w')

while True:
    txt = input('Insira o nome do arquivo: (0 para parar): ')
    if txt == '0':
        break
    else:
        arquivos.append(txt)
    
for i in arquivos:
    arq = open(i, 'r')
    for j in arq:
        saida.write(f'{j}')

arq.close()
saida.close()