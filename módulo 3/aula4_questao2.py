#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."


nota = int(input("insira a nota do filme: "))

if nota == 1:
    print("Ruim")
if nota == 2:
    print("Regular")
if nota == 3:
    print("bom!")
if nota == 4:
    print("Muito bom!")
if nota == 5:
    print("Exelente!")