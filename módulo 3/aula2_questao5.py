
idade = int(input("insira a idade:"))
genero = str(input("insira o genero: "))
trabalho = int(input("insira o tempo de trabalho: "))

a = (idade >= 60 and genero == "F" ) or (idade >= 65 and genero == "M")
b = trabalho >= 30
c = idade = 60 and trabalho >= 25

pode = a or b or c 

