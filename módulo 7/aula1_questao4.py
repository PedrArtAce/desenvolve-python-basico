frase = str(input("Insira a frase: "))
indice = []
indice_n = 0
for i in range(len(frase)):
    if frase[i] in "AEIOUaeiou":
        indice.append(i)
        indice_n += 1 

print(f"Vogais:{indice_n}")
print(f"indice:{indice}")
