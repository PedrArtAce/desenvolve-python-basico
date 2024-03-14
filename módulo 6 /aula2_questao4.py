
linter = []
l1 = []
l2 = []

nl1 = int(input("Insira o tamanho da lista 1: "))

for i in range(nl1):
    l1.append( int(input("Insira um elemento: ")))



nl2 = int(input("Insira o tamanho da lista 2: "))

for i in range(nl2):
    l2.append( int(input("Insira um elemento: ")))

if nl1 >= nl2:
    n = nl1

else:
    n = nl2

for i in range(n):
    linter.append(l1[i])
    linter.append(l2[i])

print(linter)



