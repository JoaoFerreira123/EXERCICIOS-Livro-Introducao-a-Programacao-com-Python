#Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
#Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
#Considere que o aluno cursa apenas três matérias, 
#e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2 e materia3

reprovado = False
for i in range(3):
    nota = int(input(f'Insira a nota da matéria {i+1}: '))
    if nota <= 7:
        reprovado = True
    

if reprovado:
    print('Reprovou')
else:
    print('Aprovado')

##############################
#custo do programa acima é O(n), daria pra fazer um O(1) com 3 variáveis

n1 = int(input('Insira a nota 1: '))
n2 = int(input('Insira a nota 2: '))
n3 = int(input('Insira a nota 3: '))

if n1 > 7 and n2 > 7 and n3 > 7:
    print('Aprovado')
else:
    print('Reprovou')