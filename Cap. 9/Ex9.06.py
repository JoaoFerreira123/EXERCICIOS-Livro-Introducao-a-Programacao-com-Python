# Modifique o Programa 9.5 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha. 
# Adicione também a opção para parar de imprimir até que se pressione a tecla Enter 
# cada vez que uma linha iniciar com . (ponto) como primeiro caractere.

with open('Ex9.06.txt', 'r') as texto:
    for linha in texto.readlines():
        if linha[0] == '=':
            print('='*40)
        if linha[0] == '.':
            input('Digite algo: ')
            print()
        else:
            print(linha)
