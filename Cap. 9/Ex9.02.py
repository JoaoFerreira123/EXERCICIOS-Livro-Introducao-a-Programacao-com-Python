# Modifique o programa do Exercício 9.1 para que receba mais dois parâmetros:
# a linha de início e a de fim para impressão. O programa deve imprimir apenas as linhas entre esses dois valores
# (incluindo as linhas de início e fim)


name = input('Digite o nome do arquivo: ')
#só funciona digitando todo o path, mesmo estando na mesma pasta
ini = int(input('Digite a linha de início: '))
fim = int(input('Digite a linha de fim: '))
arquivo = open(name, 'r')

for i in arquivo.readlines()[ini:fim]:
    print(i)

arquivo.close()
