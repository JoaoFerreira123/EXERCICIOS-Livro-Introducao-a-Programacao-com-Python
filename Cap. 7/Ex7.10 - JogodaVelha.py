# Escreva um jogo da velha para dois jogadores. 
# O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. 
# A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. 

vIni = ' * '
x = True
cont = 0
ganhou = False
tabuleiro = [
            [vIni, vIni, vIni],
            [vIni, vIni, vIni],
            [vIni, vIni, vIni],
]
while ganhou is False:
    for i in range(3):
        print()
        for j in range(3):
            print(tabuleiro[i][j], end = '')

    l = int(input('\nInsira a linha: '))
    c = int(input('Insira a coluna: '))
    if l >=1 and l <=3 and c >=1 and c <= 3:
        if tabuleiro[l-1][c-1] == vIni:
            if x == True:
                tabuleiro[l-1][c-1] = ' X '
                x = False
                cont+=1
            else:
                tabuleiro[l-1][c-1] = ' O '
                x = True
                cont+=1
        else:
            print('Posição já Ocupada')
    else:
        print('Jogada Inválida')
        break
    #linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != vIni:
            ganhou = True
    #colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] and tabuleiro[1][j] == tabuleiro[2][j] and tabuleiro[0][j] != vIni:
            ganhou = True
    #diag. princ.
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro [0][0] != vIni:
        ganhou = True
    #diag. sec. 
    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != vIni:
        ganhou = True
    if cont == 9:
        print('Velha! Nenhum dos jogadores ganhou')
        break

if ganhou == True and x == True:
    print('\nO jogador O ganhou')
elif ganhou == True and x == False:
    print(f'\nO jogador X ganhou')

for i in range(3):
    print()
    for j in range(3):
        print(tabuleiro[i][j], end = '')
        