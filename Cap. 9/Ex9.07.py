# Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado. 
# Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas. 
# Adicione na última linha de cada página o número da página atual e o nome do arquivo original

#ler o arquivo inteiro e caso o N de linhas passe de 60, ele escreve o rodape

arquivo = 'mobydick.txt'
linhas = 60
carcartere = 76
saida = open('saidaFormat.txt', 'w')

def escreve(arq, Mlinha):
    linha = 0
    with open(arq,'r') as arq:
        for i in arq.readlines():
            if linha == 60:
                saida.write('-------------------------------------------------')
            else:
                saida.write(f'{i}\n')
            linha += 1

escreve(arquivo, linhas)
saida.close()

????????????????????????????????