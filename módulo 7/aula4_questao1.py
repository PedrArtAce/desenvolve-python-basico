
import os


frase = input("Digite uma frase: ")

nome_arquivo = 'frase.txt'

diretorio_atual = os.getcwd()

caminho_completo = os.path.join(diretorio_atual, nome_arquivo)

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(frase)

print("Frase salva em", caminho_completo)