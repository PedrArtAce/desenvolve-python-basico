num_exp = int(input("insira o numero de experimentos: "))
cont = num_exp
exp = 0
total = 0


sapo = 0
rato = 0
coelho = 0


while cont > 0:
    animais = int(input("insira a quantidade de animais: "))
    tipo_exp = str(input("insira o tipo de experimento: "))
    total = total + animais
    if tipo_exp == 's':
        sapo = sapo + animais

    elif tipo_exp == 'r':
        rato = rato + animais

    elif tipo_exp == 'c':
        coelho = coelho + animais
    
    cont = cont - 1

print("total de cobaias:", total)
print("total de sapos:", sapo)
print("total de ratos:", rato)
print("total de coelhos:", coelho)

print("Porcentagem de sapos:", (sapo / total * 100), "%")
print("porcentagem de ratos:", (rato / total * 100), "%")
print("porcentagem de coelhos:", (coelho / total * 100), "%")

