# Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. 
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".
tot = 0
while True:
    cod = int(input('Insira o código do produto: '))
    v = 0
    match cod:
        case 0:
            break
        case 1:
            v = 0.5
        case 2:
            v = 1
        case 3:
            v = 4
        case 5:
            v = 7
        case 9:
            v = 8
        case _:
            print('Código Inválido')
    if v != 0:
        qtde = int(input('Insira a quantidade do produto: '))
        tot += v * qtde
print(f'O total é de R$: {tot}')