# Adicione os atributos tamanho e marca à classe Televisão. 
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes. 
# Depois, imprima o valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto).

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 'Padrão'
        self.marca = 'LG'

tv1 = Televisão()
tv1.tamanho = 'Grande'
tv1.marca = 'Samsung'

tv2 = Televisão()
tv2.tamanho = 'Pequeno'
tv2.marca = 'Desconhecida'

print(f'Tamanho: {tv1.tamanho}, Marca: {tv1.marca}')
print(f'Tamanho: {tv2.tamanho}, Marca: {tv2.marca}')

