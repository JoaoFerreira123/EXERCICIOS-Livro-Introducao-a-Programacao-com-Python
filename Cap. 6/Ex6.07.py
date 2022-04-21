# Faça um programa que leia uma expressão com parênteses. 
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta
# Exemplo: (()) -> OK
# ()()(()()) -> OK
# ()) -> ERRO
i = 0
p = list()
exp = input('Insira a expressão: ')
while i < len(exp):
    if exp[i] == '(':
        p.append(exp[i])
    if exp[i] == ')':
        if len(p) > 0:
            del(p[-1])
        else:
            p.append(')') #para ter a msg de erro
    i += 1

if len(p) == 0:
    print('Correto')
else:
    print('Incorreto')

