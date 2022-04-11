# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. 
# Exiba o total em dias.

cig = int(input('Quantos cigarros você fuma diariamente? '))
anos = int(input('Há quantos anos você fuma? '))

totCig = cig*(365*anos)
perdaDias = (totCig*10)/1440 #1 dia = 1440min
print(f'Você já perdeu {perdaDias:.1f} dias de vida')
