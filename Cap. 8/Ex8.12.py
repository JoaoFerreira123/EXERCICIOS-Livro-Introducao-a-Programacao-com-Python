# Escreva uma função que receba uma string e uma lista. 
# A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. 
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

def compara(str, lst):
    if str in ''.join(lst):
        return True
    else: 
        return False

    
lista = ['O', 'l','a']
string = 'Ola' 

print(compara(string, lista))