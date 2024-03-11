import random
import math 

n = int(input("insira a quantidade de números: "))
n2 = 0

for i in range(5):
    n2 += random.randint(100)

r = math.sqrt(n2)
print (r)



