# Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. 
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".

tot = prod = 0
while True:
    cod = int(input('Digite o código do produto: '))
    
    valor = 0
    if cod == 0:
        break
    elif cod == 1:
        valor = 0.5
    elif cod == 2:
        valor = 1
    elif cod == 3:
        valor = 4
    elif cod == 5:
        valor = 7
    elif cod == 9:
        valor = 8
    else: 
        print('Código Inválido')
    if valor != 0:
        qtde = int(input('Digite a quantidade desse produto: '))
        tot += valor * qtde
        prod += qtde
    
print(f'O total da compra dos {prod} produtos é de R$: {tot}')