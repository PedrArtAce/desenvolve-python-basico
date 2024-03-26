import os 

arquivo = open("roteiro.txt," 'r')

print("Texto das primeiras 25 linhas:")

for i in 25:
    linha = arquivo.readline()
    print(linha.strip())

arquivo.seek(0)

print("Numero de linhas:")

nlinhas = 0
for _ in arquivo:
    nlinhas += 1 

print(nlinhas)

arquivo.seek(0)

linha_maior_numero_caracteres = max(arquivo, key=len)
print("Linha com maior número de caracteres:")
print(linha_maior_numero_caracteres.strip())

arquivo.seek(0)

mencoes_nonato = arquivo.count('nonato')
mencoes_iria = arquivo.count('íria')

mencoes_nonato += arquivo.count('Nonato')
mencoes_iria += arquivo.count('Íria')

   
print("Número de menções aos nomes dos personagens 'Nonato' e 'Íria':")
print("Nonato:", mencoes_nonato)
print("Íria:", mencoes_iria)
