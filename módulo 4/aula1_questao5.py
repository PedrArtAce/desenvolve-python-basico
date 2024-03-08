n = int(input("Insira o numero de participantes: "))
cont = n 
idade = 0
m = 0
while cont > 0:
    idade = int(input("Inisira a idade: "))
    m = m + idade
    cont = cont - 1 
m = m / n
print (m)