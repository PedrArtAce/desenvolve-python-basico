import random

l1 = []
l2 = []
interseccção = []

for i in range (20):
    l1.append(random.randint(0, 50))
    l2.append(random.randint(0, 50))


for i in l1:
    if i in l2:
        interseccção.append(i) 

print(l1)
print(l2)

for i in interseccção:
    print(f"{i}: ({l1.count(i)}), ({l2.count(i)})")