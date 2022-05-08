# Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, 
# além do mínimo, ela vá para o canal máximo. 
# Se mudarmos para cima, além do canal máximo, que volte ao canal mínimo.


class Televisão:
    def __init__(self, canalIni, min, max):
        self.ligada = False
        self.tamanho = 'Padrão'
        self.marca = 'LG'
        self.canal = canalIni
        self.canalMin = min 
        self.canalMax = max

    def muda_canal_baixo(self):
        if self.canal -1 >= self.canalMin:
            self.canal -= 1
        else:
            self.canal = self.canalMax
    def muda_canal_cima(self):
        if self.canal +1 <= self.canalMax:
            self.canal += 1
        else:
            self.canal = self.canalMin

tv1 = Televisão(2, 2, 20) #inicia no 4, o min é 2 e o max é 20
print(f'Canal: {tv1.canal}')
tv1.muda_canal_baixo()
print(f'Canal: {tv1.canal}')
