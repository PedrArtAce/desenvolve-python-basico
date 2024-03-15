import random
cont = 1
l1 = []
for i in range(random.randint(4, 10)):
    nl1 = int(input(f"insira o numero de posição {cont}"))
    l1.append(nl1)
    cont += 1 

print(l1)
print(l1 [0:3])
print(l1 [-3:])
lpar = []

for i in l1:
    if i % 2 == 0:
        lpar.append(i)

print(lpar)

limpar = []

for i in l1:
    if i % 2 != 0:
        limpar.append(i)

print(limpar)

