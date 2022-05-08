# Atualmente, a classe Televisão inicializa o canal com 2. 
# Modifique a classe Televisão de forma a receber o canal inicial em seu construtor

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
    def muda_canal_cima(self):
        if self.canal +1 <= self.canalMax:
            self.canal += 1

tv1 = Televisão(4, 2, 20) #inicia no 4, o min é 2 e o max é 20
print(f'Canal: {tv1.canal}')
tv1.muda_canal_cima()
print(f'Canal: {tv1.canal}')
