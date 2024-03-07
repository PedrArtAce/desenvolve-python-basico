

classe = str(input("Escolha a classe (guerreiro, mago ou arqueiro): "))
força = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    pode = força >= 15 and magia <= 10 
    print (pode)
if classe == "mago":
    pode = força <= 10 and magia >= 15
    print (pode)
if classe == "arqueiro":
    pode = (força > 5 and força < 15) and (magia > 5 and magia < 15)
    print (pode)




