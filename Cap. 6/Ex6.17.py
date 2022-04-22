# Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
# Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque.

estoque = {"tomate": [100, 2.30], 
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]
}

while True:
    produto = input('Qual o produto? (0 para sair) ')
    if  produto in estoque:
        quantidade = int(input('Insira a quantidade do  produto: '))
        if quantidade <= estoque[produto][0]:
            total = 0
            print('Vendas: \n')
        
            preco = estoque[produto][1] 
            custo = preco * quantidade
            print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Quantidade solicitada não disponível')

        print(f'Custo total: {total:21.2f}\n')
        print('Estoque:\n')

        for chave, dados in estoque.items():
            print('Descrição: ', chave)
            print('Qauntidade: ', dados[0])
            print(f'Preço: {dados[1]:6.2f}\n')
    elif produto == '0':
        break
    else:
        print('Produto Não Cadastrado\n')