frase = str(input ("insira a frase: "))
espaço = 0 
for i in range(len(frase)):
    if frase[i] == " " :
        espaço += 1

print(espaço)