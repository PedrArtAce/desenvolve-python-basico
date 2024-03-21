from collections import Counter

def encontrar_anagramas(frase, objetivo):
  
    frase_lower = frase.lower()
    objetivo_lower = objetivo.lower()

  
    objetivo_contador = Counter(objetivo_lower)

    anagramas = []

    palavras = frase_lower.split()

    for palavra in palavras:
        palavra_contador = Counter(palavra)

        if palavra_contador == objetivo_contador:
            anagramas.append(palavra)

    return anagramas

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

# Encontrar e exibir os anagramas
anagramas = encontrar_anagramas(frase, objetivo)
print("Anagramas:", anagramas)