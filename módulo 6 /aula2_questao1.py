import random
maior = float('-inf')
menor =  float('inf')

l1 = []
for i in range (20):

    n = random.randint(-100, 100)

    if n > maior:
        maior = n

    elif n < menor:
        menor = n

    l1.append(n)

print (l1)
l1.sort()
print(l1)
print(f"maior {maior}")
print(f"menor {menor}")


