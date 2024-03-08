n = int(input("insira n: "))
maior = 0 
while n > 0:
    x = int(input("Insira x: "))
    if x > maior:
        maior = x 
    n = n - 1
print (maior)