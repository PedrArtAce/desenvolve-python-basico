#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
#Dica: usando listas você não precisa fazer um "if" para cada mês.
#Ex:
#Digite uma data de nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
data =[]

dia = (input("Insira a o dia do nascimento"))
mes = int(input("Insira a o mes do nascimento"))
ano = (input("Insira a o ano do nascimento"))
data.append(dia)
data.append(mes)
data.append(ano) 

mes_ex = meses[mes - 1]

print(f'Seu nascimento é dia {dia} de {mes_ex} de {ano} ')
