import random

num_elementos = random.randint(5, 20)
l1 = []

for i in range(num_elementos):
    n = random.randint(1, 10)
    l1.append(n)

print(num_elementos)
print(l1)
sum(l1)

media = sum(l1) / num_elementos
print(media)
