frase = str(input("insira a frase"))
lista = [i for i in frase]
vog = "AEIOUaeiou"
filtvog = [ i for i in lista if i in vog]
filtcons = [ i for i in lista if i not in vog and not i ==  ' ']
print(f"vogais: {filtvog}")
print(f"consoantes: {filtcons}")