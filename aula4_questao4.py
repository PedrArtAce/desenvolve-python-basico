#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int(input("insira a distancia: "))
peso = int(input("insira o peso: "))

if peso < 10:
    if distancia < 100:
        print(peso, "R$")
    if distancia > 101 and distancia < 300:
        print(peso * 1.5, "R$")
    if distancia > 300:
        print(peso * 2, "R$")
else:
    if distancia < 100:
        print(peso + 10, "R$")
    if distancia > 101 and distancia < 300:
        print(peso * 1.5 + 10, "R$")
    if distancia > 300:
        print(peso * 2 + 10, "R$")


