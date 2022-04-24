# Modifique o Programa 7.2 de forma a utilizar uma lista de palavras. 
# No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula: 
# indice = (número * 776) % len(lista_de_palavras) 

palavras = ['abacaxi','morango', 'uva', 'banana', 'amora', 'manga', 'pêssego', 'pera']
num = int(input('Digite um número: '))
indice = (num * 776) % len(palavras)

palavra = palavras[indice]
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Parabéns, você acertou!!')
        break
    tentativa = input('Digite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já digitou essa letra')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou')

##daqui pra cima é a lógica para funcionar
##daqui pra baixo é o "desenho" do bonequinho da forca, sem utilidade prática

    print("X==:==\nX  : ") 
    print("X  O " if erros >= 1 else "X")
    linha2 = ''
    if erros == 2:
        linha2 = ' | '
    elif erros == 3:
        linha2 = ' \|  '
    elif erros >= 4:
        linha2 = ' \|/ '
    print(f'X{linha2}')
    linha3 = ''
    if erros == 5:
        linha3 += ' /  '
    elif erros >= 6:
        linha3 += ' / \ '
    print(f'X{linha3}')
    print( "X\n==========")
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra era {palavra}')
        break
