# Escreva uma função para validar uma variável string. 
# Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. 
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso contrário.

def validar(str, min, max):
    if len(str) > max or len(str) < min:
        return False
    else:
        return True

string = 'Teste1234'

print(validar(string, 2, 9))