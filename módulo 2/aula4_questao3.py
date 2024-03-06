#print ("\x1B[3m", "produto", "\x1B[0m")
prod1 = str(input( "Digite o nome do produto 1: "))
prod1val = float(input( "Digite o preço unitário do produto 1: "))
prod1quan = int(input( "Digite a quantidade do produto 1: "))

prod2 = str(input( "Digite o nome do produto 2: "))
prod2val = float(input( "Digite o preço unitário do produto 2: "))
prod2quan = int(input( "Digite a quantidade do produto 2: "))

prod3 = str(input( "Digite o nome do produto 3: "))
prod3val = float(input( "Digite o preço unitário do produto 3: "))
prod3quan = int(input( "Digite a quantidade do produto 3: "))

valtot = (prod1val * prod1quan) + (prod2val * prod2quan) + (prod3val * prod3quan)

print (' o valor final é:', valtot)