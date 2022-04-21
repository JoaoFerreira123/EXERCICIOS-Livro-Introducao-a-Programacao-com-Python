# Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
# Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.
# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa

ultimo = 10 #qtde inicial de clientes na fila
fila = list(range(1, ultimo+1))

i = 0
sair = False
while True:
    print(f"\nExisteM {len(fila)} clientes na fila") 
    print(f"Fila atual: {fila}") 
    print("Digite F para adicionar um cliente ao fim da fila, ")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input('Operação: (F, A, ou S): ').upper()
    tam = len(operacao)
    while i < tam:
        if operacao[i] == 'A':
            if len(fila) > 0:
                atendido = fila.pop()
                print(f'Cliente {atendido} atendido')
            else:
                print('Fila vazia!')
        elif operacao[i] == 'F':
            ultimo +=1 #incrementa o número de elementos na fila
            fila.append(ultimo)
        elif operacao[i] == 'S':
            sair = True
            break
        else:
            print( "Operação inválida! Digite apenas F, A ou S!")
        i += 1
    if sair:
        break

#Outra opção, sem usar mais um while, seria usando FOR
#bastaria contar quantas vezes cada letra aparece na string
#E usar um FOR para repetir as adições e remoções quantas vezes fossem necessárias