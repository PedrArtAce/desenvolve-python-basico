not1 = int(input("Insira a nota 1: "))
not2 = int(input("Insira a nota 2: "))
not3 = int(input("Insira a nota 3: "))

m = (not1, not2, not3) / 3

if m >= 60:
    print("Aprovado")

elif m >= 40 and m < 60:
    print("Recuperação")


elif m < 40:
    print("reprovado")

print("Fim")