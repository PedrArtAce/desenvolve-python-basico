
idade = int(input("Qual sua idade?: "))
jogos = int(input("Quantos jogos ja jogou?: "))
vitorias = int(input("Quantos jogos ja venceu?: "))
pode = (idade >= 16 and idade <= 18) and (jogos >= 3) and (vitorias >= 1)

print(pode)

