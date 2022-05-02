# Adicione a opção de ordenar a lista por nome no menu principal.


agenda = []

def pede_nome():
    return input('Nome: ')

def pede_telefone():
    return input('Telefone: ')

def mostra_dados(nome, telefone):
    print(f'Nome: {nome} - Telefone: {telefone}')

def pede_nome_arquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print('Nome não encontrado')

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado: ')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado')

def lista():
    print('\nAgenda\n\n--------')
    for p, e in enumerate(agenda):
        print(f'Posição: {p} - ', end = '')
        mostra_dados(e[0], e[1])
    print('-------------')

def lê(): #le arquivo e grava na agenda
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r', encoding = 'utf-8') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#') #cria uma lista com nome e tel 
            agenda.append([nome, telefone])

def grava(): #le agenda e grava no arquivo
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor Inválido, favor digitar entre {inicio} e {fim}')

def menu():
    print("""
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Tamanho
    8 - Ordem Alfabética

    0 - Sai
    """)
    return valida_faixa_inteiro('Escolha uma opção: ', 0, 8)

def tamanho():
    tam = 0
    for i in agenda:
        tam += 1
    print(f'A agenda tem {tam} contatos')

def ordem():
    agenda.sort()

while True:
    opcao = menu()
    match (opcao):
        case 0:
            break
        case 1:
            novo()
        case 2:
            altera()
        case 3:
            apaga()
        case 4:
            lista()
        case 5:
            grava()
        case 6:
            lê()
        case 7:
            tamanho()
        case 8:
            ordem()