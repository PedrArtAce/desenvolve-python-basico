import os 

arquivo = open("frase.txt", 'r')
frase = arquivo.read()
arquivo.close()

texto = frase.split()
for ele in texto:
    print(ele)
