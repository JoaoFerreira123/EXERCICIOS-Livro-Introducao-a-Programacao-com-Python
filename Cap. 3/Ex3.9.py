#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#Calcule o total em segundos.
d = int(input('Insira quantos dias: '))
h = int(input('Insira quantas horas: '))
m = int(input('Insira quantos minutos: '))
s = int(input('Insira quantos segundos: '))

print(f'O total em segundos é: {s+(m*60)+(h*3600)+((d*24)*3600)}s')