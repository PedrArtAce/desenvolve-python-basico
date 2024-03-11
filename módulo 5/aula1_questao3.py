import random 

print ("advinhe um numero entre 1 e 10")
n = random.randint(1, 10)
while True:
    adv = int(input(""))
    if adv == n:
        print ("acertou!!")
        break 
    elif adv > n:
        print (" muito alto!")
    elif adv < n:
        print ("muito baixo!")

