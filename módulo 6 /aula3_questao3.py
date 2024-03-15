import random

# Gerar uma lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Imprimir a lista original
print("Lista original:")
print(lista)

# Contagem dos números negativos em cada intervalo
contagem_negativos = {}
inicio_intervalo = None
for i, num in enumerate(lista):
    if num < 0:
        if inicio_intervalo is None:
            inicio_intervalo = i
    elif inicio_intervalo is not None:
        fim_intervalo = i
        contagem_negativos[(inicio_intervalo, fim_intervalo)] = sum(1 for x in lista[inicio_intervalo:fim_intervalo] if x < 0)
        inicio_intervalo = None

# Encontrar o intervalo com a maior quantidade de números negativos
if contagem_negativos:
    intervalo_mais_negativos = max(contagem_negativos, key=contagem_negativos.get)
    del lista[intervalo_mais_negativos[0]:intervalo_mais_negativos[1]]

# Imprimir a lista após a remoção do intervalo com mais negativos
print("\nLista após deleção:")
print(lista)