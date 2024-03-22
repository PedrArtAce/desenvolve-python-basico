#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
#Ex:
#Digite uma frase: O rato roeu a roupa do rei
#Frase modificada: * r*t* r*** * r**p* d* r**


fraseinput = str(input("insira a frase: "))
frase = list(fraseinput)
vogais = "AEIOUaeiou"
vogais_list = list(vogais)

for i in frase:
    if i in vogais_list:
        fraseinput = fraseinput.replace(i, '*')

print (fraseinput)
